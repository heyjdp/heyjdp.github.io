Title: Pelican for GitHub Pages
Date: 2025-02-06 10:00
Modified: 2025-02-06 10:00
Category: Tech-Recipe
Tags: python, pelican
Slug: pelican-for-github-pages
Author: Jas Powell
Summary: Notes on Pelican setup on Github pages
Status: published 
[//]: # (comment on status: published, draft, hidden, skip)

> [!NOTE]
> The environment used for this was: Mac Air M2 8gb MacOS Sequoia 15.3

## Notes on Pelican setup on Github pages

```
pip3 install --upgrade pip
python3 -m pip install "pelican[markdown]"
mkdir -p ~/code/heyjdp.github.io
cd ~/code/heyjdp.github.io
```

Run quickstart:

```
pelican-quickstart
```

Answer questions, and then generate some basic content:

```
cat <<EOF >> content/2025-02-06-pelican-for-github-pages.md
Title: Pelican for GitHub Pages
Date: 2025-02-06 11:00
Category: Tech-Recipe

Following are some quick notes on how to use pelican for static site generation.
EOF
```

Generate and serve the site on localhost:

```
pelican content
pelican --listen
```

Browse to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Checkout all the themes:

```
cd ~/code
git clone --recursive https://github.com/getpelican/pelican-themes ~/pelican-themes
```

And enable one:

```
cd ~/code/heyjdp.github.io
nano pelicanconf.py
```

Add the line:

```
THEME="../pelican-themes/Flex"
```

And regenerate:

```
pelican content
pelican --listen
```

Modify as desired.
