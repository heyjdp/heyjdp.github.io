--- 
title: "\U0001f4bb Style9 Indent Rules on Linux/OpenBSD \U0001f427 \U0001f421 \U0001f469\u200D\U0001f4bb" 
date: 2022-03-11T11:00:00+02:00 
draft: false 
tags: ["tech", "linux", "openbsd", "development", "plan9"] 
author: "Jas" 
hidemeta: false 
disableShare: false
disableHLJS: false # This is the code highlighting
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
cover:
    image: "/post-img/c-programming-1200-628.jpg" # image path/url
    alt: "C programming indent rules from Plan 9" # alt text
#    caption: "" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: false # only hide on current single page
---

Get that lovely Plan9 source feel in your C code on Linux or OpenBSD

<!-- more -->

## Kernel Normal Form

Kernel normal form [^1], or KNF, is the coding style used in the development of code for the BSD operating systems. According to the OpenBSD man pages [^2]: 

> This file specifies the preferred style for kernel source files in the OpenBSD source tree. It is also a guide for preferred userspace code style.

KNF is based on the original KNF concept from the Computer Systems Research Group and it dictates a programming style to which contributed code should adhere prior to its inclusion into the codebase. KNF started out as a codification of how Ken Thompson and Dennis Ritchie formatted the original UNIX C source code. It describes such things as how to name variables, use indents and the use of ANSI C or K&R C code styles. Each BSD variant has its own KNF rules, which have evolved over time to differ from each other in small ways.

The SunOS kernel and userland also uses a similar indentation style that was derived from AT&T style documents and that is sometimes known as Bill Joy Normal Form. The correctness of the indentation of a list of source files can be verified by a style checker program written by Bill Shannon. This style checker program is called cstyle.

## Linux: Basically do this

From my own Debian 10 install:

```bash
$ cat /home/jas/.indent.pro 
-bap
-br
-ce
-ci4
-cli0
-d0
-di0
-i8
-ip4
-l79
-nbc
-ncdb
-ndj
-nfc1
-nlp
-npcs
-psl
-sc
-sob
```

Now just run `indent main.c` against any untidy c source file to have it indented correctly.

## BSD: Options vary slightly

According to Reddit [^3]: "Here is mine, which tries to mimic OpenBSD KNF"

```bash
-bap
-br
-ce
-ci4
-cli0
-d0
-di0
-i8
-ip
-l79
-nbc
-ncdb
-ndj
-ei
-nfc1
-nlp
-npcs
-psl
-sc
-sob
```

Similarly, run `indent *.c` against groups of untidy c source files to tidy up :)

## References

[^1]: *Kernel Normal Form*, https://en.wikipedia.org/wiki/Kernel_Normal_Form
[^2]: *Style(9) OpenBSD man pages*, https://man.openbsd.org/style.9
[^3]: *`indent(1)` rc file to format C to `style(9)` guidelines?*, https://www.reddit.com/r/openbsd/comments/ffpc7o/indent1_rc_file_to_format_c_to_style9_guidelines/
