--- 
title: "\U0001f4bb Exchanging GPG Public Keys \u26D3 \U0001f510 \U0001f469\u200D\U0001f4bb" 
date: 2022-02-03T11:00:00+02:00 
draft: false 
tags: ["tech", "crypto", "gpg", "email", "privacy"] 
# author: "Jas" 
hidemeta: false 
disableShare: false
disableHLJS: false # This is the code highlighting
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
cover:
    image: "/post-img/elaborate-key-1200x630.jpg" # image path/url
    alt: "Elaborate looking key on an old leather desk blotter" # alt text
#    caption: "" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: false # only hide on current single page
---

This guide is part of my series: The Ultimate Guide to GPG for Email Security. This particular page is about creating new keys for the GnuPG program on your computer.

<!--more-->

The Ultimate Guide to GPG Series can be found here:

- [The Ultimate Guide to GPG for Email Security](/2022/02/the-ultimate-guide-to-gpg-for-email-security/)

## How to export your own GPG public key

One of the easiest ways to get your own public key is via a command line. First find your own key finger print with the `--list-keys` (or `-k`) command:

```bash
$ gpg --list-keys
/Users/jas/.gnupg/pubring.kbx
-----------------------------
pub   ed25519/0x97350083B861B66A 2022-02-24 [SC] [expires: 2072-02-12]
      Key fingerprint = A1D1 1351 0A1E 68CA FF6C  5798 9735 0083 B861 B66A
uid                   [ultimate] Jas D Powell <jas@davepowell.net>
sub   cv25519/0xCDEC82D1091C8781 2022-02-24 [E] [expires: 2024-02-24]
sub   ed25519/0x3EABAD70AA17837B 2022-02-24 [A] [expires: 2024-02-24]
sub   ed25519/0xC94421E14BB1BF25 2022-02-24 [S] [expires: 2024-02-24]
```

And now we can export the public key:

```bash
$ gpg --export A1D113510A1E68CAFF6C579897350083B861B66A
-----BEGIN PGP PUBLIC KEY BLOCK-----

mDMEYhckDhYJKwYBBAHaRw8BAQdABbPXnYKW6u8Oyi10oyDPRNMD904yGgJ/9x3J
shgobM20IUphcyBEIFBvd2VsbCA8amFzQGRhdmVwb3dlbGwubmV0PoiRBBMWCgA5
FiEEodETUQoeaMr/bFeYlzUAg7hhtmoFAmIXJA4CGwMFCV38DwAECwkIBwQVCgkI
AhYAAh4BAheAAAoJEJc1AIO4YbZqmHEBAJzCRup6mO2OfZgxf0LzmBXiEk8lBttY
duAm9F5bRgMHAP9UPQrGBoNRgn4E+yC0JFKsGFJnu8tduZr3AH0MCYRTDbg4BGIX
JHwSCisGAQQBl1UBBQEBB0Ddwjkk4WGmJxkacHVLz3xNKhr1DpizGrseQsBdFdo/
KgMBCAeIfgQYFgoAJhYhBKHRE1EKHmjK/2xXmJc1AIO4YbZqBQJiFyR8AhsMBQkD
wmcAAAoJEJc1AIO4YbZqdhsA/A/rDcKigRyuDBV+WTJYZ/rQFEup5IpcIkozaVxv
8VmuAQCROYlml7iF5Ze/rPY2WMOVMw2+Q9BbVtQtHNuIIgyAD7gzBGIXJIwWCSsG
AQQB2kcPAQEHQMMSn4SoYCYuS2P1mhJ93sqGOv6QLaZxXIViuCoAi409iH4EGBYK
ACYWIQSh0RNRCh5oyv9sV5iXNQCDuGG2agUCYhckjAIbIAUJA8JnAAAKCRCXNQCD
uGG2apKwAQDqQuTW7Pss3nxXp4H3bf1Jf6SCKla7rvGA4Y6Bk3y0CgEA+YUW7x/Q
elPUAq5u009f6fX2zkX58oUuKUT78aqPXAK4MwRiFySRFgkrBgEEAdpHDwEBB0Cq
WoA/PVgql7VSpj6psGlQnYoTlcMKmY/I58XyRlWtCIj1BBgWCgAmFiEEodETUQoe
aMr/bFeYlzUAg7hhtmoFAmIXJJECGwIFCQPCZwAAgQkQlzUAg7hhtmp2IAQZFgoA
HRYhBIvADVIGt+CHeznpNslEIeFLsb8lBQJiFySRAAoJEMlEIeFLsb8lK+wBAP15
/qjwHzTIMlxbuueHedS3FtlKdnoYzCyfy6elDAe+AQDuZ3AaUhf/zsIAm/UV7yIc
CyQyLHCVXi9h9ybnz5ZwDeCIAP4ns/uINNYX+JBm32YkkcghonRGaneju3zR/egW
qjqHNgD/a35Uio0232b3K3htv3bXVY0EaJUq2ML/FhC+FDr8hwU=
=tqR4
-----END PGP PUBLIC KEY BLOCK-----
```

It is usually more convenient to send this to a file you can attach to an email though:

```bash
$ gpg --export A1D113510A1E68CAFF6C579897350083B861B66A > A1D113510A1E68CAFF6C579897350083B861B66A.pub
```

Now you can send the `A1D113510A1E68CAFF6C579897350083B861B66A.pub` file to anyone as an email attachment.

## How to import another public key

When you want to import a public key to your keyring, you will use the `--import` command. Let's try this out. My friend Ellen just sent me this public key `2165F1D36061645E9C5758D6C4BA55D2A32ED559.pub`. I will import it into my keyring as follows:

```bash
$ gpg --import 2165F1D36061645E9C5758D6C4BA55D2A32ED559.pub
gpg: key 0xC4BA55D2A32ED559: "Ellen Ripley <ripley@nostromo.weyland-yutani.com>" not changed
gpg: Total number processed: 1
gpg:              unchanged: 1
```

And that's it. We can now send encrypted and signed messages to Ellen.
