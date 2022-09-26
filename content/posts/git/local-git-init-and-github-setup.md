--- 
title: "\U0001f4bb Local Git init and GitHub setup \U0001f419 \U0001f43e \U0001f469\u200D\U0001f4bb" 
date: 2022-08-10T11:00:00+02:00 
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

A quick how-to guide to get your local `git init` project onto GitHub.

<!--more-->

## Create some code

On your local machine you started a project and now you decided that you want to upload it to GitHub. First we need to check that we are configured for git:

```bash
$ git config -l
color.ui=true
user.name=heyjdp
user.email=dave@davepowell.net
user.signingkey=7367E3012B4F6A98D2BD9D4DF43BA3EA4862E172
diff.colormoved=zebra
init.defaultbranch=main
pull.rebase=true
fetch.prune=true
```

**NOTE:** The `pull.rebase=true` can be a bit controversial, especially if signing commits

Now we can run git init in the root directory of the project:

```bash
$ git init
Initialized empty Git repository in /home/dave/code/terraform-ansible-aws-wireguard/.git/
```

## Start a project with the same name on GitHub

Head over to GitHub and start a new project:

![Start a new project with the same name in GitHub](/post-img/github-new-project.jpg)

At this stage I like to include a MIT or BSD 3-clause license.

## Make a `.gitignore`

Do it now, before you `git add` a whole bunch of stuff you didn't mean to

### Remove `.DS_Store` from the repo (MacOS)

If you havve accidentally already committed a project with `.DS_Store` files in it, don't worry, we can fix that. To remove the .DS_Store files from the repo run this:

```bash
find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch
```

Make sure to include `.DS_Store` in the `.gitignore` file. Use this command in the git root directory:

```bash
echo .DS_Store >> .gitignore
```

Now commit the file to the repository:

```bash
git add .gitignore
git commit -m '.DS_Store has been removed'
```

## Initial commit

You now need to make the initial commit locally before we set the origin server and pull/push the code:

```bash
$ git add .
$ git commit -m "Initial commit"
[master (root-commit) 5cefecc] Initial push, using Nginx template
 15 files changed, 451 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 LICENSE
 create mode 100644 README.md
 create mode 100644 src/ansible.cfg
 create mode 100644 src/aws-server.yaml
 create mode 100644 src/datasources.tf
 create mode 100644 src/main.tf
 create mode 100644 src/providers.tf
 create mode 100644 src/roles/base/tasks/main.yaml
 create mode 100644 src/roles/harden/tasks/main.yaml
 create mode 100644 src/roles/harden/templates/20auto-upgrades.j2
 create mode 100644 src/roles/harden/templates/jail.local.j2
 create mode 100644 src/roles/nginx/tasks/main.yaml
 create mode 100644 src/terraform.tfvars
 create mode 100644 src/variables.tf
```

## Change git default branch from master to main

Do this to make the default branch called `main`:

```bash
$ git branch -M main
```

## Set the origin

```bash
$ git remote add origin git@github.com:heyjdp/terraform-ansible-aws-wireguard.git
```

And push the files upstream:

```bash
$ git push -u origin main
Enumerating objects: 26, done.
Counting objects: 100% (26/26), done.
Delta compression using up to 8 threads
Compressing objects: 100% (20/20), done.
Writing objects: 100% (26/26), 5.31 KiB | 906.00 KiB/s, done.
Total 26 (delta 0), reused 0 (delta 0)
To github.com:heyjdp/terraform-ansible-aws-wireguard.git
 + e66332d...5cefecc main -> main (forced update)
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

## For an existing project

**Note:** the above only works because this is a new project with no branches yet, for an existing project you might want to do this:

```bash
# create main branch locally, taking the history from master
git branch -m master main

# push the new local main branch to the remote repo (GitHub) 
git push -u origin main

# switch the current HEAD to the main branch
git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main

# change the default branch on GitHub to main
# https://docs.github.com/en/github/administering-a-repository/setting-the-default-branch

# delete the master branch on the remote
git push origin --delete master
```

## The `github.com` reference

### Create a new repository on the command line

```bash
echo "# My New Project" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:heyjdp/my-new-project.git
git push -u origin main
```

### Push an existing repository from the command line

```bash
git remote add origin git@github.com:heyjdp/my-new-project.git
git branch -M main
git push -u origin main
```

## References

- https://stevenmortimer.com/5-steps-to-change-github-default-branch-from-master-to-main/
- https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-to-push-an-existing-project-to-GitHub
- https://stackoverflow.com/questions/107701/how-can-i-remove-ds-store-files-from-a-git-repository
