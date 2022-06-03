--- 
title: "\U0001f4bb Installing and Configuring GPG \u26D3 \U0001f510 \U0001f469\u200D\U0001f4bb" 
date: 2021-12-19T11:00:00+02:00 
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

This guide is part of my series: The Ultimate Guide to GPG for Email Security. This particular page is about installing and configuring the GPG program on your computer.

<!--more-->

The Ultimate Guide to GPG Series can be found here:

- [The Ultimate Guide to GPG for Email Security](/2021/11/the-ultimate-guide-to-gpg-for-email-security/)

## Installing GPG on MacOS

Go and install [gpgtools for Mac OS](https://gpgtools.org/). That is all for now.

## Configuring `gnupg` on Mac OS

After you install `gpg` on the Mac you will find a file: `$HOME/.gnupg/gpg.conf`. Change it to look like this:

```txt
auto-key-retrieve
no-emit-version
no-comments
no-greeting
charset utf-8
fixed-list-mode
keyid-format 0xlong
list-options show-uid-validity
verify-options show-uid-validity
require-cross-certification
no-symkey-cache
throw-keyids
use-agent
armor

personal-cipher-preferences AES256 AES192 AES
personal-digest-preferences SHA512 SHA384 SHA256
personal-compress-preferences Uncompressed
default-preference-list SHA512 SHA384 SHA256 AES256 AES192 AES Uncompressed
cert-digest-algo SHA512
s2k-cipher-algo AES256
s2k-digest-algo SHA512
s2k-mode 3
s2k-count 65011712

disable-cipher-algo 3DES
weak-digest SHA1
force-mdc
```
