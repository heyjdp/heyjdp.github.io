--- 
title: "\U0001f4bb Yocto Linux build for Raspberry Pi 4 \U0001f353 \U0001f967 \U0001f469\u200D\U0001f4bb" 
date: 2023-01-27T13:00:00+02:00 
draft: false 
tags: ["tech", "linux", "yocto", "raspberry-pi", "development", "hardware"] 
hidemeta: false 
disableShare: false
disableHLJS: false # This is the code highlighting
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
cover:
    image: "/post-img/yocto-1200x628.jpg" # image path/url
    alt: "Raspberry Pi header with power wires" # alt text
#    caption: "" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: false # only hide on current single page
---

Let's build our own Linux operating system for a Raspberry Pi 4

<!-- more -->

First we need a big build box, something 16 VPC and 32GB RAM from AWS should do the trick. I like this machine:

- c4.4xlarge
- 

## Set up the development environment

```bash
sudo apt update && sudo apt -qy dist-upgrade && sudo apt -qy install gawk wget git diffstat unzip texinfo gcc-multilib build-essential chrpath socat libsdl1.2-dev xterm sed cvs subversion coreutils texi2html docbook-utils python-pysqlite2 help2man desktop-file-utils libgl1-mesa-dev libglu1-mesa-dev mercurial autoconf automake groff curl lzop asciidoc u-boot-tools cpio sudo rsync linux-headers-$(uname -r) locales
```

Additional requirements:

```
sudo apt -qy install python python3 python3-pip python3-pexpect python3-git xz-utils debianutils iputils-ping zstd liblz4-tool
```

### Install `repo`

```bash
mkdir -p ~/.bin
PATH="${HOME}/.bin:${PATH}"
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/.bin/repo
chmod a+rx ~/.bin/repo
```

And persist this by adding to `$HOME/.bashrc`

```bash
export PATH="${HOME}/.bin:${PATH}"
```

### Rainbow PS1

**OPTIONAL** To make life less boring, add as last line of `$HOME/.bashrc`

```bash
export PS1="\[$(tput bold)\]\[$(tput setaf 1)\]\u\[$(tput setaf 208)\]@\[$(tput setaf 3)\h\[$(tput setaf 2)\]:\d \[$(tput setaf 4)\]\@:\[$(tput setaf 55)\]\w\n$PROMPT_COLOR\$ \[$(tput sgr0)\]"
```

## Make sure you are working on a bigdisk

See if we need a filesystem on the raw storage?



Then mount:

```
sudo mkdir /bigdisk
sudo chown ubuntu:ubuntu /bigdisk
sudo mount /dev/xvdf /bigdisk
cd /bigdisk
mkdir raspberrypi
cd raspberrypi/
```

## Set up git

```bash
git config --global user.name "builder"
git config --global user.email "builder@example.org"
```

## Clone Yocto

```
git clone git://git.yoctoproject.org/poky -b langdale
cd poky
git clone git://git.openembedded.org/openembedded-core -b langdale
git clone git://git.openembedded.org/meta-openembedded -b langdale
git clone git://git.yoctoproject.org/meta-raspberrypi -b langdale
git clone git://git.yoctoproject.org/meta-security -b langdale
source oe-init-build-env
```

## Edit your conf

`nano conf/local.conf`

and add these lines:

```
MACHINE = "raspberrypi4-64"
DISTRO = "poky"

EXTRA_IMAGE_FEATURES ?= "debug-tweaks" # NOTE this is incompatible with security features
#DISTRO_FEATURES:append = " security" #NOTE enable this when the image development is finalized

USER_CLASSES ?= "buildstats"
PATCHRESOLVE = "noop"
BB_DISKMON_DIRS ??= "\
    STOPTASKS,${TMPDIR},1G,100K \
    STOPTASKS,${DL_DIR},1G,100K \
    STOPTASKS,${SSTATE_DIR},1G,100K \
    STOPTASKS,/tmp,100M,100K \
    ABORT,${TMPDIR},100M,1K \
    ABORT,${DL_DIR},100M,1K \
    ABORT,${SSTATE_DIR},100M,1K \
    ABORT,/tmp,10M,1K"
PACKAGECONFIG:append_pn-qemu-system-native = " sdl"
CONF_VERSION = "2"

#DL_DIR ?= "${TOPDIR}/downloads"
ACCEPT_FSL_EULA = "1"

# Switch to Debian packaging and include package-management in the image
PACKAGE_CLASSES = "package_deb"
#PACKAGE_FEED_URIS = "http://172.20.1.35:8000" # Enable this when you know your local IP for serving apt packages
EXTRA_IMAGE_FEATURES += "package-management" # And enable this too

LICENSE_FLAGS_ACCEPTED += "commercial "
PACKAGECONFIG_pn-gstreamer1.0-plugins-ugly += "x264"

# Additional install packages
IMAGE_INSTALL:append = " gcc g++ make dpkg-dev libc6-dev python3-fail2ban openssh" # Here is where we add packages we want built into the final image

PARALLEL_MAKE="-j16"
BB_NUMBER_THREADS="16"

INHERIT += "buildhistory"
BUILDHISTORY_COMMIT = "1"
```

All the layers can be found on this website: https://layers.openembedded.org/layerindex/branch/langdale/layers/ 

And edit `nano conf/bblayers.conf` to look like this:

```
# POKY_BBLAYERS_CONF_VERSION is increased each time build/conf/bblayers.conf
# changes incompatibly
POKY_BBLAYERS_CONF_VERSION = "2"

BBPATH = "${TOPDIR}"
BBFILES ?= ""

BBLAYERS ?= " \
  /bigdisk2/poky/meta \
  /bigdisk2/poky/meta-poky \
  /bigdisk2/poky/meta-yocto-bsp \
  /bigdisk2/poky/meta-raspberrypi \
  /bigdisk2/poky/meta-openembedded/meta-oe \
  /bigdisk2/poky/meta-openembedded/meta-networking \
  /bigdisk2/poky/meta-openembedded/meta-filesystems \
  /bigdisk2/poky/meta-openembedded/meta-multimedia \
  /bigdisk2/poky/meta-openembedded/meta-python \
  /bigdisk2/poky/meta-openembedded/meta-gnome \
  /bigdisk2/poky/meta-openembedded/meta-xfce \
  /bigdisk2/poky/meta-security \
  "
```

Then run:

```
#bitbake core-image-full-cmdline
bitbake core-image-minimal-xfce
```

## Write the SD card

You will find the `.wic.bz2` file in `./tmp/deploy/images/raspberrypi4-64/`

Copy it your local machine, `bzcat` the file and then `dd` the `.wic` to the SD card

Boot up the Pi4 and you should have XFCE4 and also `ssh` access

## References

[^1]: https://tutorialadda.com/yocto/create-your-own-linux-image-for-the-raspberry-pi-board-using-yocto-project
[^2]: https://low-level.wiki/yocto/honister-upgrade.html 