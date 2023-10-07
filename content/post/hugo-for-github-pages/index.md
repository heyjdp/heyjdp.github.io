---
title: "Hugo for GitHub Pages"
date: 2023-10-07
draft: false
categories:
  - Backend & Cloud Engineering
tags:
  - hugo
  - github-pages
  - static-site
  - ci-cd
description: "A step-by-step guide to setting up Hugo with BeautifulHugo and GitHub Pages, from install to automated deployment via GitHub Actions."
image: "post/hugo-for-github-pages/featured.jpeg"
---

> **Environment:** Mac M2 8GB & macOS

I was recently asked for a method to stand up a staic site blog, and using GitHub Pages is a pretty easy way to make that happen without hosting fees or managing the underlying machine. Here is my step-by-step.

Hugo is written in Go, it's really fast, and it can deploy to GitHub Pages via Actions. Here are my notes.

## Install Hugo

On macOS, Homebrew is the path of least resistance:

```bash
brew install hugo
hugo version
```

You want the `extended` version (Homebrew gives you this by default). It includes SCSS/SASS support, which most themes need.

## Create the Site

```bash
mkdir -p ~/code/heyjdp.github.io
cd ~/code/heyjdp.github.io
hugo new site . --force
```

The `--force` flag lets Hugo initialise in a non-empty directory (useful if you've already got a README or `.gitignore` in there).

This gives you the skeleton:

```
.
├── archetypes/
├── content/
├── data/
├── hugo.toml
├── layouts/
├── static/
└── themes/
```

## Initialise Git

```bash
git init
git add -A
git commit -m "chore: hugo new site"
```

## Add a Theme

I'm using BeautifulHugo [1]. It's clean, readable, handles code blocks well, and doesn't try to do too much. Add it as a git submodule so your builds are reproducible:

```bash
git submodule add https://github.com/halogenica/beautifulhugo.git themes/beautifulhugo
```

Pin it to a specific commit so you're not surprised by upstream changes:

```bash
cd themes/beautifulhugo
git log -1 --format="%H"    # grab the latest SHA
cd ../..
```

Now tell Hugo to use it. Edit `hugo.toml`:

```toml
baseURL       = "https://heyjdp.github.io/"
languageCode  = "en-us"
title         = "Dr Jas Powell"
theme         = "beautifulhugo"

pygmentsCodeFences  = true
pygmentsUseClasses  = true

[Params]
  subtitle   = "Engineering Management & Leadership"
  selfHosted = true
  useHLJS    = false

[taxonomies]
  category = "categories"
  tag      = "tags"

[[menu.main]]
  name   = "Blog"
  url    = "/"
  weight = 1

[[menu.main]]
  name   = "About"
  url    = "/page/about/"
  weight = 2

[[menu.main]]
  name   = "Tags"
  url    = "/tags/"
  weight = 3
```

The `selfHosted = true` flag is important - it tells BeautifulHugo to serve fonts and icons locally instead of pulling from Google Fonts and CDNs. No third-party requests, no GDPR headaches.

## Create Your First Post

```bash
mkdir -p content/post/hello-world
cat <<'EOF' > content/post/hello-world/index.md
---
title: "Hello World"
date: 2023-10-07
draft: false
tags:
  - meta
description: "First post. Testing the plumbing."
---

First post. If you can read this, Hugo and GitHub Pages are working.
EOF
```

Hugo uses page bundles - each post gets its own directory under `content/post/`. This keeps images and other assets co-located with the post that uses them.

## Build and Preview Locally

```bash
hugo serve
```

Browse to [http://localhost:1313](http://localhost:1313). Hugo's live reload is genuinely fast - save a file and the browser updates before you can alt-tab to it. If the live reloading is giving you a problem, try these options:

- Disable Fast Render: Run hugo server --disableFastRender to force Hugo to rebuild more pages when files change.
- Bypass HTTP Cache: Run hugo server --noHTTPCache so your browser or server doesn't load old cached versions.

```bash
hugo server --disableFastRender --noHTTPCache
```

To do a full production build (minified, no drafts):

```bash
hugo --minify
```

Output lands in `public/`. Don't commit this directory - GitHub Actions will build it for you.

Add it to `.gitignore`:

```bash
echo "public/" >> .gitignore
echo ".hugo_build.lock" >> .gitignore
```

## Deploy with GitHub Actions

This is the bit that makes Hugo on GitHub a great option for static hosted websites. Just push to `main` and GitHub handles the rest.

Create the workflow file:

```bash
mkdir -p .github/workflows
```

And add `.github/workflows/hugo.yml`:

```yaml
name: Deploy Hugo site to GitHub Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          submodules: recursive
          fetch-depth: 0

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: 'latest'
          extended: true

      - name: Build
        run: hugo --minify

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v2
        with:
          path: ./public

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
```

A few things to note:

- `submodules: recursive` - essential, otherwise your theme won't be checked out and the build will fail with a cryptic error about missing layouts.
- `fetch-depth: 0` - needed if you use `enableGitInfo = true` in your config (Hugo can show last-modified dates from git history).
- `extended: true` - you want Hugo Extended for SCSS support.

## GitHub Repo Settings

One manual step. Go to your repo on GitHub:

**Settings - Pages - Build and deployment - Source - GitHub Actions**

This tells GitHub to use the Actions workflow instead of the legacy branch-based deployment. If you skip this step, your workflow will run but nothing will actually deploy.

1. Go to https://github.com/heyjdp/heyjdp.github.io/settings/pages
2. Under "Build and deployment" - "Source", change it from "Deploy from a branch" to "GitHub Actions"
3. Once saved, re-run your Hugo workflow (or just push a commit) and the site should go live

## Push and Watch It Go

```bash
git add -A
git commit -m "feat: initial hugo site with github actions deployment"
git remote add origin git@github.com:heyjdp/heyjdp.github.io.git
git push -u origin main
```

Give it a minute or two. Check the Actions tab in your repo to watch the build. Once the green tick appears, your site is live at `https://heyjdp.github.io`.

## What I Like About This Setup

- **Speed.** Hugo builds this site in under 100ms. Pelican took seconds. For a small blog that's academic, but it makes the local dev loop genuinely pleasant.
- **Single binary.** No virtualenv, no pip dependencies, no Python version juggling. `brew install hugo` and you're done.
- **Git submodule for the theme.** Pin it to a commit. Reproducible. No surprises.
- **GitHub Actions.** Push to main, site deploys. No `ghp-import`, no separate `gh-pages` branch to manage.

The whole thing took about an hour to set up from scratch, and most of that was fiddling with the `hugo.toml` config until I was happy with the menu layout.

## References

1. [BeautifulHugo theme](https://github.com/halogenica/beautifulhugo)
2. [Hugo Quick Start](https://gohugo.io/getting-started/quick-start/)
3. [Hugo - Hosting on GitHub](https://gohugo.io/hosting-and-deployment/hosting-on-github/)
