--- 
title: "\U0001f4bb Send and Receive GPG Email on MacOS \u26D3 \U0001f510 \U0001f469\u200D\U0001f4bb" 
date: 2022-02-25T11:00:00+02:00 
draft: false 
tags: ["tech", "crypto", "gpg", "email", "privacy"] 
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

- [The Ultimate Guide to GPG for Email Security](/2021/11/the-ultimate-guide-to-gpg-for-email-security/)

## How to Install a Secure Email Client for MacOS

Well, actually, you may have already done this. There is a standard secure email plugin that is installed with the default settings when you install [GPGTools](gpgtools.org).

The easiest way to check whether this was installed or not is to just start up the Mac Mail App...

## Sending an encrypted GnuPG email in Mail.app in MacOS

The OpenPGP plugin for Mail.app on MacOS looks like the normal Mail.app with two main differences. Look at the picture below on the right side...

a) There is a drop down to choose the OpenPGP plugin. If it is not showing there, it is not installed correctly. Reinstall [GPGTools Suite for Mac](gpgtools.org).

b) If you cannot see both icons showing pink as in the image below then you are not encrypting and signing the message.

![Using MacOS Mail.app to send an encrypted and signed email](/post-img/sending-gpg-email-on-macos.jpg)

**IMPORTANT NOTE** only signing is switched on by default. By default the OpenPGP plugin does *not* encrypt outbound messages. You have to CLICK THE LOCK to encrypt the message.

**NOTE** In case you didn't understand, this is not secure by default. You have to remember to import the other parties public key and click the lock.

## Receiving an encrypted GnuPG Email in Mail.app on MacOS

One of the nice features of the GnuPG Mail plugin for MacOS is that there is no additional complexity when recieving email. As you can see in the screenshot below, the mail was opened for reading automatically, and it is confirmed to be encrypted and signed by the Dave Powell key.

![Using MacOS Mail.app to receive an encrypted and signed email](/post-img/recieving-gpg-email-on-macos.jpg)

**IMPORTANT NOTE** because of the way the GPG encryption works, if I had not made my own email account a cc (or a bcc) to the email, then I would not have been able to open the email. You have to remember to include yourself on your own emails. Unless that is a security threat for you.

**NOTE** So seriously, you can't read your own send email unless you cc/bcc yourself to every email you send from now on!

## Receiving an encrypted GnuPG Email in GMail

Mostly I use GMail in a browser. As a big command-line user I actually find it easier to use the shell to make an encrypted message, cut/paste it to the browser, send the email, receive an encrypted blob in the browser, cut/paste to the shell. Let me show you:

![Using GMail in the web browser to receive an encrypted email](/post-img/recieving-gpg-email-on-gmail.jpg)

As you can see the email appears to have no content, but there are two attachments, one is called `noname` and the other is called `encrypted.asc`. Let's download them and see what they contain.

```bash
$ cat noname
Version: 1
```

So, the small attachment seems to be a versioning token. Nothing to see here. Let's check to see if we can decrypt the other file:

```bash
$ gpg -d encrypted.asc
Content-Type: multipart/signed;
	boundary="Apple-Mail=_35EC6387-E7A6-433E-8E82-5EC61C6886C8";
	protocol="application/pgp-signature";
	micalg=pgp-sha512


--Apple-Mail=_35EC6387-E7A6-433E-8E82-5EC61C6886C8
Content-Transfer-Encoding: quoted-printable
Content-Type: text/plain;
	charset=us-ascii

Hi Ellen,

I hope you are having a lovely flight. I imagine you will not read this =
mail for another couple of decades, but all is well here on Earth.

Best regards.

Dave

PS - Practice with that power loader, it will come in handy!

--Apple-Mail=_35EC6387-E7A6-433E-8E82-5EC61C6886C8
Content-Disposition: attachment;
	filename=signature.asc
Content-Type: application/pgp-signature;
	name=signature.asc
Content-Transfer-Encoding: 7bit

-----BEGIN PGP SIGNATURE-----

iHUEARYKAB0WIQSLwA1SBrfgh3s56TbJRCHhS7G/JQUCYhev6QAKCRDJRCHhS7G/
Jc4eAP9evNIEjiVMb1V6FbGniOejeRxCy55UXAknknOlmpftnwD8DR97+i0jIb2g
hrpjHfsc0YGTRu7LYHL+DLoHcSSL4gs=
=UUQ4
-----END PGP SIGNATURE-----

--Apple-Mail=_35EC6387-E7A6-433E-8E82-5EC61C6886C8--
```

Yes, we have a file attachement that we can encrypt. However, because the mail has been mangled by the plugin, we cannot verify the signature:

```bash
$ gpg --verify encrypted.asc
gpg: verify signatures failed: Unexpected error
```

## Conclusion of Encrypted email with MacOS Mail.app

It really is more trouble than it is worth. The [EFF posted a blog on how to delete the Mail.app GPGTools plugin](https://www.eff.org/deeplinks/2018/05/disabling-pgp-apple-mail-gpgtools), and just use command line encryption instead. This is also my recommendation!

