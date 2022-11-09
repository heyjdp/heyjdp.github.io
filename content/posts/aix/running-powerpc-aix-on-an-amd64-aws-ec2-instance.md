--- 
title: "\U0001f4bb Running PowerPC AIX on AMD64 AWS EC2 \U0001f469\u200D\U0001f4bb \U0001f4a5 \U0001f528" 
date: 2022-11-01T20:00:00+02:00 
draft: true 
tags: ["tech", "unix", "aix", "aws", "ec2", "hack"] 
hidemeta: false 
disableShare: false
disableHLJS: false # This is the code highlighting
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
cover:
    image: "/post-img/ibm-8286-42a-aix-pseries-1200-630.jpg" # image path/url
    alt: "An IBM pSeries server running AIX operating system" # alt text
#    caption: "" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: false # only hide on current single page
---

It shouldn't really be possible to boot, install and run IBMs proprietory PowerPC Unix on the public cloud, but I did it anyway...

<!--more-->

## Getting started

Alright, so I won't get into **why** I needed a copy of IBMs `AIX_7.X` running in a terminal on a Power8, but I did. So let's focus on what happened next, and not why it happened...

So, obvs I started on `.torrent`, and I found a copy of `AIX_7.1`, both install DVDs - w00t, so I download then (obvs with hard upload limits, because this is AIX). 

Next I spin up a `C4.2xlarge` on AWS mainly because 
 1. I ran out of NVMe on my Lenovo laptop, and 
 2. because if we are going to do this we might as well go hard.

To the untrained eye, this may seem like a piece of cake, like that time I made a OpenBSD installer for AWS Xen (even though the internet said 'it can't be done'), but you see the main differenvce is that the OpenBSD installer has a x86_64/amd64 variant.

AIX does not.

AIX only runs on IBMs p-series PowerPC chipsets.

So we need to trans* the instruction set. As Mike from Spaced said: "Let's play...!"

!["Let's play...!", said Mike from Spaced](/post-img/mike-spaced.jpg)

### QEMU on AWS

Piece of cake, get a fast machine and build from scratch. Debian as a Base O/S is not a shit solution, find the AMI here [^1]. For Frankfurt `eu-central-1` the AMI is `ami-082e96a7dd15bd594`

Let's fire up a AWS EC2 instance of `c4.2xlarge` with options, SSH access from 0.0.0.0/0 in the security group and an extra 100GB gp3 disk to be mounted after boot, and then run this all :-

Log in:
```bash
ssh -vv -i andle-key-001.pem -o "UserKnownHostsFile=/dev/null" -o "StrictHostKeyChecking=no" admin@3.67.40.153
```

Mount the disk[^4]:
```bash
admin@ip-172-31-10-10:~$ lsblk
NAME     MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
xvda     202:0    0    8G  0 disk 
├─xvda1  202:1    0  7.9G  0 part /
├─xvda14 202:14   0    3M  0 part 
└─xvda15 202:15   0  124M  0 part /boot/efi
xvdb     202:16   0  100G  0 disk 
admin@ip-172-31-10-10:~$ sudo file -s /dev/xvdb
/dev/xvdb: data
admin@ip-172-31-10-10:~$ sudo mkfs -t xfs /dev/xvdb
mkfs: failed to execute mkfs.xfs: No such file or directory
admin@ip-172-31-10-10:~$ sudo apt update && sudo apt -qy install xfsprogs
Get:1 http://cdn-aws.deb.debian.org/debian bullseye InRelease [116 kB]
Get:2 http://cdn-aws.deb.debian.org/debian bullseye-updates InRelease [44.1 kB]
Get:3 http://cdn-aws.deb.debian.org/debian bullseye-backports InRelease [49.0 kB]
<---snip--->

admin@ip-172-31-10-10:~$ sudo mkfs -t xfs /dev/xvdb
meta-data=/dev/xvdb              isize=512    agcount=4, agsize=6553600 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=1, sparse=1, rmapbt=0
         =                       reflink=1    bigtime=0
data     =                       bsize=4096   blocks=26214400, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0, ftype=1
log      =internal log           bsize=4096   blocks=12800, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
admin@ip-172-31-10-10:~$ sudo mkdir /data
admin@ip-172-31-10-10:~$ sudo mount /dev/xvdb /data
admin@ip-172-31-10-10:~$ sudo chown -R admin:admin /data
admin@ip-172-31-10-10:~$ cd /data
admin@ip-172-31-10-10:/data$ echo hello > temp.txt
admin@ip-172-31-10-10:/data$ cat temp.txt 
hello
```

Security basics (update the packages and add `fail2ban` to avoid `ssh` hammering):
```bash
admin@ip-172-31-10-10:/data$ sudo apt update && sudo apt -qy upgrade
<---snip--->

dmin@ip-172-31-10-10:/data$ sudo apt -qy install fail2ban
Reading package lists...
Building dependency tree...
Reading state information...
The following additional packages will be installed:
  python3-pyinotify python3-systemd whois
Suggested packages:
  mailx monit sqlite3 python-pyinotify-doc
The following NEW packages will be installed:
  fail2ban python3-pyinotify python3-systemd whois
<---snip--->
```

Install all dependencies:
```bash
admin@ip-172-31-10-10:/data$ sudo apt -qy install git build-essential meson telnet
admin@ip-172-31-10-10:/data$ sudo apt -qy install git-email libaio-dev libbluetooth-dev libcapstone-dev libbrlapi-dev libbz2-dev
admin@ip-172-31-10-10:/data$ sudo apt -qy install libcap-ng-dev libcurl4-gnutls-dev libgtk-3-dev libibverbs-dev libjpeg62-turbo-dev libncurses5-dev libnuma-dev
admin@ip-172-31-10-10:/data$ sudo apt -qy install librbd-dev librdmacm-dev libsasl2-dev libsdl2-dev libseccomp-dev libsnappy-dev libssh-dev
admin@ip-172-31-10-10:/data$ sudo apt -qy install libvde-dev libvdeplug-dev libvte-2.91-dev libxen-dev liblzo2-dev valgrind xfslibs-dev libnfs-dev libiscsi-dev
```

Make sure you are building QEMU from source on the disk with plenty of space, I used QEMU v7.1.0[^6]:
```bash
admin@ip-172-31-10-10:/data$ cd /data 
admin@ip-172-31-10-10:/data$ git clone git://git.qemu-project.org/qemu.git
Cloning into 'qemu'...
remote: Counting objects: 646623, done.
<---snip--->

admin@ip-172-31-10-10:/data$ cd qemu
admin@ip-172-31-10-10:/data/qemu$ git submodule init
Submodule 'dtc' (https://gitlab.com/qemu-project/dtc.git) registered for path 'dtc'
<---snip--->

admin@ip-172-31-10-10:/data/qemu$ git submodule update --recursive
Cloning into '/data/qemu/dtc'...
Submodule path 'dtc': checked out 'b6910bec11614980a21e46fbccc35934b671bd81'
<---snip--->

admin@ip-172-31-10-10:/data/qemu$ git submodule status --recursive
 b6910bec11614980a21e46fbccc35934b671bd81 dtc (v1.6.1)
<---snip--->

admin@ip-172-31-10-10:/data/qemu$ mkdir build; cd build
admin@ip-172-31-10-10:/data/qemu/build$ ../configure
admin@ip-172-31-10-10:/data/qemu/build$ make -j$(nproc)
```

And now wait some minutes for the server to compile and link 10,000 objects :) I found the instructions for the QEMU build ont he official wiki[^2].

Now we install it:
```bash
admin@ip-172-31-10-10:/data/qemu/build$ sudo su
root@ip-172-31-10-10:/data/qemu/build# make install
  GIT     ui/keycodemapdb meson tests/fp/berkeley-testfloat-3 tests/fp/berkeley-softfloat-3 dtc
[1/153] Generating qemu-version.h with a custom command (wrapped by meson to capture output)
[2/35] Generating tests/include/QAPI test (include) with a custom command
[2/3] Installing files.
Installing trace/trace-events-all to /usr/local/share/qemu
Installing fsdev/virtfs-proxy-helper to /usr/local/libexec
<---snip--->
```

### AIX_7.1 doesn't support virtio *facepalm*

Now, I `scp` my AIX_7.1.iso file to the `/data` partition on AWS from local:
```bash
$ scp -i andle-key-001.pem -o "StrictHostKeyChecking=no" ./Downloads/AIX_v7.1_Install_DVD_1_of_2.iso admin@3.67.40.153:/data/710000.iso
```

And then on the AWS machine make a root disk for QEMU to use like so:
```bash
admin@ip-172-31-10-10:/~$ ca /data
admin@ip-172-31-10-10:/data$ qemu-img create -f  qcow2  hdisk0.qcow2  20G
```

Now, we run the VM. So now you will want a second terminal into AWS open because we are going to `telnet` into the serial device so we have a terminal emulator. In the first terminal, enter this:
```bash
admin@ip-172-31-10-10:/data$ qemu-system-ppc64 -cpu power8 -smp 2 -machine pseries -m 4096 -drive file=hdisk0.qcow2,if=none,id=drive-virtio-disk0 -device virtio-scsi-pci,id=scsi -device scsi-hd,drive=drive-virtio-disk0 -cdrom 710000.iso -prom-env "boot-command=boot cdrom:" -prom-env "input-device=/vdevice/vty@71000000" -prom-env "output-device=/vdevice/vty@71000000" -nographic -monitor stdio -serial telnet:localhost:4321,server,nowait
```

And nice and quickly, in the second terminal enter the following:
```bash
admin@ip-172-31-10-10:/data$ telnet localhost 4321
```

Unfortunately though, AIX 7.1 WILL NOT BOOT on QEMU *cry*

There is a bug report here[^3], I see exactly the same result, the installer dies before it starts up fully with:
```bash
  Welcome to Open Firmware

  Copyright (c) 2004, 2017 IBM Corporation All rights reserved.
  This program and the accompanying materials are made available
  under the terms of the BSD License available at
  http://www.opensource.org/licenses/bsd-license.php

Trying to load: -s verbose from: /vdevice/v-scsi@71000003/disk@8200000000000000:\ppc\chrp\bootfile.exe ...   Successfully loaded
AIX
StarLED{814}

AIX Version 7.1
exec(/etc/init){1,0}
<---snip--->

Illegal Trap Instruction Interrupt in Kernel
05911ACC            tweqi    r0,0                r0=0
KDB(0)>
```

After some investigation on the web I find some messages that tell me that AIX didn't include support for virtio until AIX_7.2, so now I need to find a copy of that...

### How I downloaded AIX_7.2

Well, see the thing is that your not supposed to have a copy of AIX unless you are a IBM customer with a) hardware to run AIX and b) an unexpired AIX license. Some fuckery was required...

Let's talk hypothetically for a moment, let's say, hypothetically, that if I wanted to obtain some unobtainium, then, hypothetically speaking:

 1. I could go to the IBM ESS (Entitled Systems Support) website, and make an account
 2. then look on eBay for a pSeries server to buy (something with a Power8 processor is still in date)
 3. examine all the pSeries pictures on eBay until I got some serial numbers for the servers
 4. typed the models and serial numbers into the 'My Machines' box on the ESS website, until I found one that did not have an unexpired license
 5. noted the customer number associated with the entitled server (where the number is 9 digits, the first three are the country code, and the last 6 are the customer ID)
 6. verified the customer ID via the serial number of the entitled server
 7. Went to the downloads page and downloaded the AIX_7.2 installation DVDs

 All hypothetically speaking, of course. Don't do this though. Stealing is theft!

### Installation and the Boot Loop



### References

[^1]: https://wiki.debian.org/Cloud/AmazonEC2Image/Bullseye, Community AMI for Debian
[^2]: https://en.wikibooks.org/wiki/QEMU/Installing_QEMU, QEMU from source
[^3]: https://lists.gnu.org/archive/html/qemu-devel/2019-09/msg02329.html, [Qemu-devel] issue related to boot aix 7.1 when I try to use qemu ppc64
[^4]: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html, Mount EBS on AWS EC2 instance
[^5]: https://kwakousys.wordpress.com/2020/09/06/run-aix-7-2-on-x86-with-qemu/, a nice recipe from another site 
[^6]: https://github.com/qemu/qemu/releases/tag/v7.1.0, QEMU v7.1.0 sourceqemu/qemu/releases/tag/v7.1.0, QEMU v7.1.0 source
[^7]: http://aix4admins.blogspot.com/2020/04/qemu-aix-on-x86-qemu-quick-emulator-is.html, Another AIX on QEMU recipe (didn't really work, claims it is using 7.1, but didn't run for me)