--- 
title: "\U0001f4bb The Ultimate Guide to GPG for Email Security \u26D3 \U0001f510 \U0001f469\u200D\U0001f4bb" 
date: 2021-11-25T11:00:00+02:00 
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

There are many guides on the web for setting up GPG keys. Most of the one I have come across are outdated, or simply incorrect. This is an attempt to right those wrongs.

<!--more-->

## What is GPG?

[GPG (GnuPG)](gnupg.org) is a hybrid-encryption software program. GPG is a free-software replacement for [Symantec's PGP](https://en.wikipedia.org/wiki/Pretty_Good_Privacy) cryptographic software suite. The GnuPG software is compliant with [RFC 4880](https://datatracker.ietf.org/doc/html/rfc4880), the IETF standards-track specification of OpenPGP. Hybrid because it uses a combination of conventional symmetric-key cryptography for speed, and public-key cryptography for secure key exchange. The key exchange method is called Diffie-Hellman and, typically by using the recipient's public key to encrypt a session key which is used only once. This mode of operation is part of the OpenPGP standard and has been part of PGP from its first version.

## What is it for?

The business-level answer to this question is that we usually use GPG to send secrets between team members in a distributed or remote work environment. E.g. if the CEO needs to give me the company credit card details to sign the company up for a corporate GitHub account, I will:

- Send the CEO instructions on how to install `gpg` and configure it for the best security
- Send the CEO instructions on how to make their own public and private keys
- Send the CEO my public key, and request theirs in return
- Send the CEO instructions on how to install secure email client and insert their keys
- Ask the CEO to make an encrypted email to me containing the secret credit card information that I need

It may seem like a lot of work, but let's all remember that email is all **plain text** in flight and **plain text** at rest on the server, and so many companies have lost so much IP and more from having their email hacked or leaked on-line.

**BASIC RULE** do not send secrets in plain text email

**BASIC TRUTH** it doesn't matter if Google Mail has a little padlock in the browser, the body text of the email is **not** encrypted, the email is stored as a `.txt` file on someone else's computer. And if you work in a large organization, it is likely that the IT team subverted the `https` connection anyway to make sure you are not stealing company secrets. Do not trust email.

There is a more thorough technical-level answer to the question that involves encrypted storage of company secrets, encrypted code repositories, encrypted backups, and signed code commits. But, for now, let's stick to the email use case.

## Are there any downsides to using GPG for email encryption?

Yes! Basically if your email is fully encrypted then you lose the ability to search in your email contents - because it is all encrypted and we only unwrap one message at a time.

Why is this a bad thing?

Well, basically people then realize that the email title is not encrypted and start putting more and more useful and search-able information into the email subject line, and that can compromise the systems that you are trying to protect by encrypting the information.

Consider an encrypted email between senior systems administrators that had a title _"Secret log server logbot@logbot.company.com port 5060 password inside"_. I mean, sure we don't know that password, it is in the email body that is encrypted, but we have just been given the user, machine DNS and log system port in the title. A crackers job just became a lot simpler.

## The full GPG installation and configuration guide

This post got really long, so I have broken it into more manageable parts:

1. [Installing and Configuring GPG](/2021/12/installing-and-configuring-gpg/)
2. [Create new GPG master and subkeys](/2022/01/create-gnupg-master-keys-and-subkeys/)
3. [Exchanging GPG public keys](/2022/02/exchanging-gpg-public-keys/)
4. [Send/Receive GnuPG Emails on MacOS](/2022/02/send-and-receive-gpg-email-on-macos/)

## References

- [1] https://ryandaniels.ca/blog/upgrade-ssh-keys-gpg-agent-ed25519/
- [2] https://blog.josefsson.org/tag/ed25519/
- [3] https://musigma.blog/2021/05/09/gpg-ssh-ed25519.html
- [4] https://news.ycombinator.com/item?id=13382734
- [5] https://alexcabal.com/creating-the-perfect-gpg-keypair 
- [6] https://www.digitalneanderthal.com/post/gpg/ 
- [7] http://irtfweb.ifa.hawaii.edu/~lockhart/gpg/ 
- [8] https://security.stackexchange.com/questions/25170/what-information-is-leaked-from-an-openpgp-encrypted-file
- [9] https://github.com/SixArm/gpg-encrypt 
- [10] https://davesteele.github.io/gpg/2014/09/20/anatomy-of-a-gpg-key/ 
- [11] https://dev.gnupg.org/T5590 
- [12] https://security.stackexchange.com/questions/254045/gnupg-now-uses-ecc-25519-as-default-on-new-key-generation-any-compatibility-is 
- [13] https://incenp.org/notes/2015/using-an-offline-gnupg-master-key.html 
- [14] https://gist.github.com/MorganGeek/5e6b89d351d34dfbc576db610b0c02e8 