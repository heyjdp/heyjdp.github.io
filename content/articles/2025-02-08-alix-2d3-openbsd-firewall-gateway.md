Title: Alix 2D3 OpenBSD Firewall Gateway
Date: 2025-02-08 10:00
Modified: 2025-02-08 10:00
Category: Tech-Recipe
Tags: alix2d3, openbsd, firewall, gateway
Slug: alix-2d3-openbsd-firewall-gateway
Author: Jas Powell
Summary: Notes on Setup of an Alix 2D3 with OpenBSD to act as a Firewall/Gateway
Status: published 
[//]: # (comment on status: published, draft, hidden, skip)

> [!NOTE]
> The environment used for this was: Mac Air M2 8gb MacOS Sequoia 15.3

## Notes on Setup of an Alix 2D3 with OpenBSD to act as a Firewall/Gateway

### Download and verify:

Get a copy of OpenBSD, in this case the `amd64` install image. From here: [https://cdn.openbsd.org/pub/OpenBSD/7.6/amd64/](https://cdn.openbsd.org/pub/OpenBSD/7.6/amd64/)

And make sure to check the `sha256sum` against the published value[^1]:

```sh
sha256sum ./Downloads/install76.img
973dfa837e4998f6c0f29d0afc9f40d85e29a3d2b25fcea8b3f13b4491fbedc0  ./Downloads/install76.img
```

### Create install media

Insert a USB stick into the Macbook:

```sh
diskutil list
/dev/disk4 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *62.5 GB    disk4
   1:                       0xEF                         491.5 KB   disk4s1
   2:                    OpenBSD                         729.3 MB   disk4s4
                    (free space)                         61.8 GB    -
```

Our external disk is `/dev/disk4` - so now we can copy the install image, unmount the disk first:

```sh
diskutil unmountDisk /dev/disk4
sudo dd if=./Downloads/install76.img of=/dev/disk4 bs=1m
```

### Boot the Alix 2D3

First you need a serial cable, insert it into the serial port of the Alix (powered off) and also into the USB port of the Macbook. You need to identify the serial device:

```sh
ls /dev/cu.*
/dev/cu.usbserial-11210
```

So now we can make a screen connection to the serial port. Note that the default baud rate is 38400, but it can be set in the BIOS to 115200:

```sh
screen /dev/cu.usbserial-11210 115200
```

NOTE: to leave a `screen` session press `CTRL+a`, `k` then `y`

Insert the USB device into the Alix 2D3 and put the power onto the Alix 2D3. You will see a screen like this:

```sh
SeaBIOS (version ?-20160307_153453-michael-desktop64)
XHCI init on dev 00:10.0: regs @ 0xfeb22000, 4 ports, 32 slots, 32 byte contexts
XHCI    extcap 0x1 @ feb22500
XHCI    protocol USB  3.00, 2 ports (offset 1), def 0
XHCI    protocol USB  2.00, 2 ports (offset 3), def 10
XHCI    extcap 0xa @ feb22540
Found 2 serial ports
ATA controller 1 at 4010/4020/0 (irq 0 dev 88)
EHCI init on dev 00:13.0 (regs=0xfeb25420)
ATA controller 2 at 4018/4024/0 (irq 0 dev 88)
Searching bootorder for: /pci@i0cf8/*@14,7
Searching bootorder for: /rom@img/memtest
Searching bootorder for: /rom@img/setup
ata0-0: KINGSTON SMS200S330G ATA-8 Hard-Disk (28626 MiBytes)
Searching bootorder for: /pci@i0cf8/*@11/drive@0/disk@0
XHCI port #3: 0x00200e03, powered, enabled, pls 0, speed 3 [High]
Searching bootorder for: /pci@i0cf8/usb@10/storage@3/*@0/*@0,0
Searching bootorder for: /pci@i0cf8/usb@10/usb-*@3
USB MSC vendor='SSK' product='USB3.2' rev='' type=0 removable=1
USB MSC blksize=512 sectors=122136576
Initialized USB HUB (0 ports used)
All threads complete.
Scan for option roms
PCengines Press F10 key now for boot menu:
```

Note that to press F10 on the Macbook Air you need to press fn+F10...

```sh
Select boot device:

1. USB MSC Drive SSK USB3.2
2. ata0-0: KINGSTON SMS200S330G ATA-8 Hard-Disk (28626 MiBytes
3. Payload [memtest]
4. Payload [setup]
```

### Install OpenBSD

First of all, we need to stop the Alix going into a boot loop over the serial console. Select the USB drive from the boot menu, then do this:

```sh
Booting from Hard Disk...
Booting from 0000:7c00
Using drive 0, partition 3.
Loading......
probing: pc0 com0 com1 mem[638K 1918M a20=on]
disk: hd0+ hd1+
>> OpenBSD/amd64 BOOT 3.67
boot> stty com0 115200
boot> set tty com0
switching console to com0
>> OpenBSD/amd64 BOOT 3.67
boot> bsd.rd
```

The important lines are:

```sh
boot> stty com0 115200
boot> set tty com0
boot> bsd.rd
```

You should get to this point, at which stage you can follow any OpenBSD install guide, but it is very simple:

```sh
Welcome to the OpenBSD/amd64 7.6 installation program.
WARNING: / was not properly unmounted
(I)nstall, (U)pgrade, (A)utoinstall or (S)hell?
```

Press `I` to install and follow onscreen instructions, note that NIC `em0` is the one closest to the serial port.

```sh
WARNING: / was not properly unmounted
(I)nstall, (U)pgrade, (A)utoinstall or (S)hell? I
At any prompt except password prompts you can escape to a shell by
typing '!'. Default answers are shown in []'s and are selected by
pressing RETURN.  You can exit this program at any time by pressing
Control-C, but this can leave your system in an inconsistent state.

Terminal type? [vt220]
System hostname? (short form, e.g. 'foo') cappuccino

Available network interfaces are: em0 em1 em2 vlan0.
Network interface to configure? (name, lladdr, '?', or 'done') [em0]
IPv4 address for em0? (or 'autoconf' or 'none') [autoconf]
IPv6 address for em0? (or 'autoconf' or 'none') [none]
Available network interfaces are: em0 em1 em2 vlan0.
Network interface to configure? (name, lladdr, '?', or 'done') [done]
Using DNS domainname my.domain
Using DNS nameservers at 213.140.210.232 213.140.211.232

Password for root account? (will not echo)
Password for root account? (again)
Start sshd(8) by default? [yes]
Change the default console to com0? [yes]
Available speeds are: 9600 19200 38400 57600 115200.
Which speed should com0 use? (or 'done') [115200]
Setup a user? (enter a lower-case loginname, or 'no') [no] jas
Full name for user jas? [jas]
Password for user jas? (will not echo)
Password for user jas? (again)
WARNING: root is targeted by password guessing attacks, pubkeys are safer.
Allow root ssh login? (yes, no, prohibit-password) [no]
What timezone are you in? ('?' for list) [Asia/Nicosia]

Available disks are: sd0 sd1.
Which disk is the root disk? ('?' for details) [sd0]
Encrypt the root disk with a (p)assphrase or (k)eydisk? [no]
Disk: sd0       geometry: 3649/255/63 [58626288 Sectors]
Offset: 0       Signature: 0xAA55
            Starting         Ending         LBA Info:
 #: id      C   H   S -      C   H   S [       start:        size ]
-------------------------------------------------------------------------------
 0: 00      0   0   0 -      0   0   0 [           0:           0 ] Unused
 1: 00      0   0   0 -      0   0   0 [           0:           0 ] Unused
 2: 00      0   0   0 -      0   0   0 [           0:           0 ] Unused
*3: A6      0   1   2 -   3648 254  63 [          64:    58621121 ] OpenBSD
Use (W)hole disk MBR, whole disk (G)PT, (O)penBSD area or (E)dit? [OpenBSD]
The auto-allocated layout for sd0 is:
#                size           offset  fstype [fsize bsize   cpg]
  a:          1004.7M               64  4.2BSD   2048 16384     1 # /
  b:          1789.4M          2057632    swap
  c:         28626.1M                0  unused
  d:          1487.5M          5722240  4.2BSD   2048 16384     1 # /tmp
  e:          2302.2M          8768576  4.2BSD   2048 16384     1 # /var
  f:          3209.3M         13483392  4.2BSD   2048 16384     1 # /usr
  g:           896.8M         20056128  4.2BSD   2048 16384     1 # /usr/X11R6
  h:          3588.0M         21892768  4.2BSD   2048 16384     1 # /usr/local
  i:          2389.9M         29241056  4.2BSD   2048 16384     1 # /usr/src
  j:          5803.7M         34135488  4.2BSD   2048 16384     1 # /usr/obj
  k:          6152.2M         46021536  4.2BSD   2048 16384     1 # /home
Use (A)uto layout, (E)dit auto layout, or create (C)ustom layout? [a]
/dev/rsd0a: 1004.7MB in 2057568 sectors of 512 bytes
5 cylinder groups of 202.50MB, 12960 blocks, 25920 inodes each
/dev/rsd0k: 6152.2MB in 12599648 sectors of 512 bytes
31 cylinder groups of 202.50MB, 12960 blocks, 25920 inodes each
/dev/rsd0d: 1487.5MB in 3046336 sectors of 512 bytes
8 cylinder groups of 202.50MB, 12960 blocks, 25920 inodes each
/dev/rsd0f: 3209.3MB in 6572736 sectors of 512 bytes
16 cylinder groups of 202.50MB, 12960 blocks, 25920 inodes each
/dev/rsd0g: 896.8MB in 1836640 sectors of 512 bytes
5 cylinder groups of 202.50MB, 12960 blocks, 25920 inodes each
/dev/rsd0h: 3588.0MB in 7348288 sectors of 512 bytes
18 cylinder groups of 202.50MB, 12960 blocks, 25920 inodes each
/dev/rsd0j: 5803.7MB in 11886048 sectors of 512 bytes
29 cylinder groups of 202.50MB, 12960 blocks, 25920 inodes each
/dev/rsd0i: 2389.9MB in 4894432 sectors of 512 bytes
12 cylinder groups of 202.50MB, 12960 blocks, 25920 inodes each
/dev/rsd0e: 2302.2MB in 4714816 sectors of 512 bytes
12 cylinder groups of 202.50MB, 12960 blocks, 25920 inodes each
Available disks are: sd1.
Which disk do you wish to initialize? (or 'done') [done]
/dev/sd0a (52d29e0dc555db56.a) on /mnt type ffs (rw, asynchronous, local)
/dev/sd0k (52d29e0dc555db56.k) on /mnt/home type ffs (rw, asynchronous, local, nodev, nosuid)
/dev/sd0d (52d29e0dc555db56.d) on /mnt/tmp type ffs (rw, asynchronous, local, nodev, nosuid)
/dev/sd0f (52d29e0dc555db56.f) on /mnt/usr type ffs (rw, asynchronous, local, nodev)
/dev/sd0g (52d29e0dc555db56.g) on /mnt/usr/X11R6 type ffs (rw, asynchronous, local, nodev)
/dev/sd0h (52d29e0dc555db56.h) on /mnt/usr/local type ffs (rw, asynchronous, local, nodev)
/dev/sd0j (52d29e0dc555db56.j) on /mnt/usr/obj type ffs (rw, asynchronous, local, nodev, nosuid)
/dev/sd0i (52d29e0dc555db56.i) on /mnt/usr/src type ffs (rw, asynchronous, local, nodev, nosuid)
/dev/sd0e (52d29e0dc555db56.e) on /mnt/var type ffs (rw, asynchronous, local, nodev, nosuid)

Let's install the sets!
Location of sets? (disk http nfs or 'done') [http] disk
Is the disk partition already mounted? [no]
Available disks are: sd0 sd1.
Which disk contains the install media? (or 'done') [sd1]
  a:          1424384             1024  4.2BSD   2048 16384 16142
  i:              960               64   MSDOS
Available sd1 partitions are: a i.
Which sd1 partition has the install sets? (or 'done') [a]
Pathname to the sets? (or 'done') [7.6/amd64]

Select sets by entering a set name, a file name pattern or 'all'. De-select
sets by prepending a '-', e.g.: '-game*'. Selected sets are labelled '[X]'.
    [X] bsd           [X] base76.tgz    [X] game76.tgz    [X] xfont76.tgz
    [X] bsd.mp        [X] comp76.tgz    [X] xbase76.tgz   [X] xserv76.tgz
    [X] bsd.rd        [X] man76.tgz     [X] xshare76.tgz
Set name(s)? (or 'abort' or 'done') [done] -x* -game
    [X] bsd           [X] base76.tgz    [X] game76.tgz    [ ] xfont76.tgz
    [X] bsd.mp        [X] comp76.tgz    [ ] xbase76.tgz   [ ] xserv76.tgz
    [X] bsd.rd        [X] man76.tgz     [ ] xshare76.tgz
Set name(s)? (or 'abort' or 'done') [done]
Directory does not contain SHA256.sig. Continue without verification? [no] yes
Installing bsd          100% |**************************| 28007 KB    00:01
Installing bsd.mp       100% |**************************| 28139 KB    00:01
Installing bsd.rd       100% |**************************|  4600 KB    00:00
Installing base76.tgz   100% |**************************|   414 MB    00:54
Extracting etc.tgz      100% |**************************|   264 KB    00:00
Installing comp76.tgz   100% |**************************| 81512 KB    00:18
Installing man76.tgz    100% |**************************|  8039 KB    00:02
Installing game76.tgz   100% |**************************|  2746 KB    00:00
Installing BUILDINFO    100% |**************************|    54       00:00
Location of sets? (disk http nfs or 'done') [done]
Saving configuration files... done.
Making all device nodes... done.
Multiprocessor machine; using bsd.mp instead of bsd.
fw_update: add amd; update none
Relinking to create unique kernel... done.

CONGRATULATIONS! Your OpenBSD install has been successfully completed!

When you login to your new system the first time, please read your mail
using the 'mail' command.

Exit to (S)hell, (H)alt or (R)eboot? [reboot]
```

Remove the install media and reboot.

### Configuration

First run, do the following to update (run as root, use `su`):

```sh
syspatch
pkg_add -Uu
sysmerge -d
fw_update
reboot
```

Add `nano` because who has the time to deal with arrow-keys not being arrow-keys

```sh
pkg_add nano
```

Now, edit the `doas` users:

```sh
nano /etc/doas.conf
```

And insert the line:

```sh
permit nopass :wheel
```

Now you should log in as the user account (in the `wheel` group), and then use `doas su` to perform root operations.

### Shutdown un-needed services

We don't need `smtpd` and `sndiod` on this machine, shut them down:

```sh
cappuccino# rcctl ls on
check_quotas
cron
dhcpleased
library_aslr
ntpd
pf
pflogd
resolvd
slaacd
smtpd
sndiod
sshd
syslogd

cappuccino# rcctl stop smtpd
smtpd(ok)
cappuccino# rcctl disable smtpd
cappuccino# rcctl stop sndiod
sndiod(ok)
cappuccino# rcctl disable sndiod
```

### Network setup

```sh
echo 'net.inet.ip.forwarding=1' >> /etc/sysctl.conf
echo 'inet autoconf' > /etc/hostname.em0 # or use a static IP
echo 'inet 172.20.10.1 255.255.255.0 172.20.10.255' > /etc/hostname.em1
echo 'inet 172.20.20.1 255.255.255.0 172.20.20.255' > /etc/hostname.em2
```

### dhcpd

```sh
rcctl enable dhcpd
rcctl set dhcpd flags em1 em2
nano /etc/dhcpd.conf
```

### pf Firewall config

```sh
nano /etc/pf.conf
```

And insert the following:

```sh
wired = "em1"
wifi  = "em2"
table <martians> { 0.0.0.0/8 10.0.0.0/8 127.0.0.0/8 169.254.0.0/16     \
                   172.16.0.0/12 192.0.0.0/24 192.0.2.0/24 224.0.0.0/3 \
                   192.168.0.0/16 198.18.0.0/15 198.51.100.0/24        \
                   203.0.113.0/24 }
set block-policy drop
set loginterface egress
set skip on lo0
match in all scrub (no-df random-id max-mss 1440)
match out on egress inet from !(egress:network) to any nat-to (egress:0)

match in on { $wired } inet proto { tcp udp } from any to !172.20.10.1 port 53 rdr-to 172.20.10.1
match in on { $wifi } inet proto { tcp udp } from any to !172.20.20.1 port 53 rdr-to 172.20.20.1

antispoof quick for { egress $wired $wifi }
block in quick on egress from <martians> to any

block in quick on { $wired $wifi } proto { tcp udp } from any to any port 853
block in quick on { $wired $wifi } proto { tcp udp } from any to any port 5353

block return out quick on egress from any to <martians>
block all
pass out quick inet
pass in on { $wired $wifi } inet
```

### unbound for DNS

```sh
rcctl enable unbound
nano /var/unbound/etc/unbound.conf
```

And insert the following:

```sh
server:
        interface: 172.20.10.1
        interface: 172.20.20.1
        interface: 127.0.0.1
        access-control: 172.20.10.0/24 allow
        access-control: 172.20.20.0/24 allow
        do-not-query-localhost: no
        hide-identity: yes
        hide-version: yes
        prefetch: yes

forward-zone:
        name: "."
        forward-addr: 1.1.1.1  # IP of the preferred upstream resolver
```

And make sure that the localhost interface takes DNS from the local resolver:

```sh
nano /etc/dhclient.conf
```

Add the following:

```sh
ignore domain-name, domain-name-servers;
append dhcp-lease-time 86400;
send host-name "cappuccino";
prepend domain-name-servers 127.0.0.1;
prepend domain-name "office.lan";
```

And now adjust the DHCP lease daemon:

```sh
nano /etc/dhcpleased.conf
```

Add this:

```sh
interface em0 {
        ignore dns
}
```

### Manually hammer `/etc/revolv.conf`

Note, that I didn't have much luck with this method, it seems like still the best thing to do is manually edit `/etc/resolv.conf` and then change the flags:

```sh
nano /etc/resolv.conf
```

And add this:

```sh
nameserver 127.0.0.1
lookup file bind
```

And lock the file:

```sh
chflags uchg /etc/resolv.conf
```

This can be reversed with:

```sh
chflags nouchg /etc/resolv.conf
```


## References

[^1]: [https://cdn.openbsd.org/pub/OpenBSD/7.6/amd64/SHA256](https://cdn.openbsd.org/pub/OpenBSD/7.6/amd64/SHA256)

