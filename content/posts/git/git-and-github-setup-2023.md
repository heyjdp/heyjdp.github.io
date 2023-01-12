--- 
title: "\U0001f4bb Git and GitHub Setup 2023 \U0001f419 \U0001f43e \U0001f469\u200D\U0001f4bb" 
date: 2023-01-11T16:00:00+02:00 
draft: false 
tags: ["tech", "git", "github", "development"] 
hidemeta: false 
disableShare: false
disableHLJS: false # This is the code highlighting
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
cover:
    image: "/post-img/github-1200x630.jpg" # image path/url
    alt: "The GitHub logo" # alt text
#    caption: "" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: false # only hide on current single page
---

My 2023 `git` and GitHub setup guide.

<!--more-->

## Git Setup

Set up git globally:

```bash
git config --global init.defaultbranch main
git config --global color.ui true
git config --global fetch.prune true
git config --global diff.colorMoved zebra
```

## Make a new `ssh` key

Make a ssh key for authentication:

```bash
ssh-keygen -a 100 -t ed25519 -C "jas@business.com" -f jas-business-github-key-ed25519
```

Upload the ssh key to your GitHub acount, and test with:

```bash
ssh -i jas-business-github-key-ed25519 -T git@github.com
```

And GitHub should reply with:

```
Hi jas-business! You've successfully authenticated, but GitHub does not provide shell access.
```

## Adding keys to the local `git` config

If you are git clone-ing a existing project that needs your new key[^2], use a line like this one:

```bash
ssh-agent $(ssh-add jas-business-github-key-ed25519; git clone git@github.com:user/project.git)
```

And if you work on different projects for business and for personal, in the directory of the project[^3]:

```bash
git init
git config --local user.name "jas"
git config --local user.email "jas@business.com"
git config --local core.sshCommand "ssh -i jas-business-github-key-ed25519"
```

## To rebase or not to rebase?

The rebase question:

So, previously I have recommended using this flag to force a rebase on a pull,

```bash
git config --global pull.rebase true
```

however, after investigating signed/verified git commits I came across the following advice[^1]:

> When rebasing the changes are replayed on master. This causes them to be "rebased" on a new parent commit which will change the commit-id (which is partially based on the parent commit-id).
> 
> Rebasing may also require merging the changes as the commits are replayed. Even if the merge happens automatically, it may change the contents of the files. The file contents are another element that make up the commit-id.
> 
> The verification is done through a cryptographic signature of the contents and the commit-metadata. Hence, rebasing will break that signature.
> 
> To not break your signature you'll need to use a fast-forward merge (where no new merge commit is created). To achieve that you'll need to locally rebase your changes and sign them.
> 
> Or you can squash-rebase, where all your small commits are rolled up into a single new commit, which GitHub will sign on your behalf.
> 
If verification is important to you, rebasing is generally a bad idea, fast-forward merges and merge commits will better reflect what actually happened and who had authored those changes.

## Signing (verified) git commits

Now, about signing git commits:

See this reference[^4]

## References

[^1] https://stackoverflow.com/questions/62950018/verified-signatures-are-gone-after-i-pressed-rebase-and-merge
[^2] https://stackoverflow.com/questions/4565700/how-to-specify-the-private-ssh-key-to-use-when-executing-shell-command-on-git
[^3] https://dev.to/web3coach/how-to-configure-a-local-git-repository-to-use-a-specific-ssh-key-4aml
[^4] https://calebhearth.com/sign-git-with-ssh