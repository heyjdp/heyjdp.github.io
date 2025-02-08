Title: GitHub Setup
Date: 2025-02-08 10:00
Modified: 2025-02-08 10:00
Category: Tech-Recipe
Tags: github, ssh
Slug: github-setup
Author: Jas Powell
Summary: Notes on GitHub Setup
Status: published 
[//]: # (comment on status: published, draft, hidden, skip)

> [!NOTE]
> The environment used for this was: Mac Air M2 8gb MacOS Sequoia 15.3

## Notes on GitHub Setup

General git config that works for me...

```
git config --global init.defaultbranch main
git config --global color.ui true
git config --global fetch.prune true
git config --global diff.colorMoved zebra
git config --global pull.rebase false
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

## Reset `ssh-agent` issue

So, sometimes when you run:

```bash
ssh -i jas-business-github-key-ed25519 -T git@github.com
```

And GitHub should reply with:

```
Hi jas-business! You've successfully authenticated, but GitHub does not provide shell access.
```

But instead you see:

```
Hi jas-PERSONAL! You've successfully authenticated, but GitHub does not provide shell access.
```

And you're confused because you definitely used the right key and when you run `git config user.name` you see the right user name, it may be because the `ssh-agent` got confused between terminal windows, sigh!

Do this:

```bash
killall ssh-agent; eval `ssh-agent`
```

and sanity will be restored!

## Adding keys to the local `git` config

If you are git clone-ing a existing project that needs your new key[^1], use a line like this one:

```bash
ssh-agent $(ssh-add jas-business-github-key-ed25519; git clone git@github.com:user/project.git)
```

And if you work on different projects for business and for personal, in the directory of the project[^2]:

```bash
git init
git config --local user.name "jas"
git config --local user.email "jas@business.com"
git config --local core.sshCommand "ssh -i jas-business-github-key-ed25519"
```

## References

[^1]: https://stackoverflow.com/questions/4565700/how-to-specify-the-private-ssh-key-to-use-when-executing-shell-command-on-git

[^2]: https://dev.to/web3coach/how-to-configure-a-local-git-repository-to-use-a-specific-ssh-key-4aml

