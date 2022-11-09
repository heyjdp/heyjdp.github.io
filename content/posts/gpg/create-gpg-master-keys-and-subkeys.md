--- 
title: "\U0001f4bb Create GnuPG Master Keys and Subkeys \u26D3 \U0001f510 \U0001f469\u200D\U0001f4bb" 
date: 2022-01-12T11:00:00+02:00 
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

## Use a RAM Disk

For added security, consider using a RAM Disk to create all the secret key material and export to USB from there. Later you can import only the subkeys and public keys to the local machine.

- [Use a RAM disk on MacOS for tmpfs](/2022/01/ramdisk-tmpfs-for-macos/)

## Master Keys and Subkeys

A lot of guides will tell you that it is okay to create one general purpose key and that we are all done with the keys. Okay, so this is *one* strategy. But what happens when someone takes your laptop from your car? Or when the HDD fizzles and you know you were definitely going to make a backup, but didn't...

The way we deal with this challenge is to:

- make a GPG Master key
- use that Master key to create Subkeys
- export the Master key from the computer and save it on e.g. a USB drive we can hide offline
- detatch the Master key and leave only the subkeys on the machine

This way, if anything happens to the subkeys, or the machine, we can fetch the offline USB drive and make new keys!

## Create a Master key

Try this (obvs replace the info with your own info!):

```bash
$ gpg --quick-gen-key "Jas Powell <jas@davepowell.net>" ed25519 sign 50y
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: key 0x97350083B861B66A marked as ultimately trusted
gpg: revocation certificate stored as '/Users/jas/.gnupg/openpgp-revocs.d/A1D113510A1E68CAFF6C579897350083B861B66A.rev'
public and secret key created and signed.

pub   ed25519/0x97350083B861B66A 2022-02-24 [SC] [expires: 2072-02-12]
      Key fingerprint = A1D1 1351 0A1E 68CA FF6C  5798 9735 0083 B861 B66A
uid                              Jas Powell <jas@davepowell.net>
```

Note the use of 50 years for the expiry date of they key!

Also, note that the revocation certificate for the key was automatically generated:

```txt
$ cat /Users/jas/.gnupg/openpgp-revocs.d/A1D113510A1E68CAFF6C579897350083B861B66A.rev
This is a revocation certificate for the OpenPGP key:

pub   ed25519/0x97350083B861B66A 2022-02-24 [SC] [expires: 2072-02-12]
      Key fingerprint = A1D1 1351 0A1E 68CA FF6C  5798 9735 0083 B861 B66A
uid                            Jas Powell <jas@davepowell.net>

A revocation certificate is a kind of "kill switch" to publicly
declare that a key shall not anymore be used.  It is not possible
to retract such a revocation certificate once it has been published.

Use it to revoke this key in case of a compromise or loss of
the secret key.  However, if the secret key is still accessible,
it is better to generate a new revocation certificate and give
a reason for the revocation.  For details see the description of
of the gpg command "--generate-revocation" in the GnuPG manual.

To avoid an accidental use of this file, a colon has been inserted
before the 5 dashes below.  Remove this colon with a text editor
before importing and publishing this revocation certificate.

:-----BEGIN PGP PUBLIC KEY BLOCK-----
Comment: This is a revocation certificate

iHgEIBYKACAWIQSh0RNRCh5oyv9sV5iXNQCDuGG2agUCYhckHAIdAAAKCRCXNQCD
uGG2avUkAQDfxSGmbuKu04J8guVbK84BE1LLU8HNYndIUtEc0XyvGAD/enGaGFTS
CDUisSIfuzD8hhpsb1FGNcDTb/Ib+Q1n7Ag=
=j+io
-----END PGP PUBLIC KEY BLOCK-----
```

## Create Subkeys

Let's find the ID of the key we just made, list the public keys (lowercase `k`):

```bash
$ gpg -k
/Users/jas/.gnupg/pubring.kbx
-----------------------------
pub   ed25519/0x97350083B861B66A 2022-02-24 [SC] [expires: 2072-02-12]
      Key fingerprint = A1D1 1351 0A1E 68CA FF6C  5798 9735 0083 B861 B66A
uid                   [ultimate] Jas Powell <jas@davepowell.net>
```

And list the secret/private keys (uppercase `k`):

```bash
$ gpg -K
/Users/jas/.gnupg/pubring.kbx
-----------------------------
sec   ed25519/0x97350083B861B66A 2022-02-24 [SC] [expires: 2072-02-12]
      Key fingerprint = A1D1 1351 0A1E 68CA FF6C  5798 9735 0083 B861 B66A
uid                   [ultimate] Jas Powell <jas@davepowell.net>
```

Our key fingerprint is `A1D113510A1E68CAFF6C579897350083B861B66A`, so let's use this to create subkeys:

```bash
gpg --quick-add-key A1D113510A1E68CAFF6C579897350083B861B66A cv25519 encr 2y
gpg --quick-add-key A1D113510A1E68CAFF6C579897350083B861B66A ed25519 auth 2y
gpg --quick-add-key A1D113510A1E68CAFF6C579897350083B861B66A ed25519 sign 2y
```

Now when we list the public keys we can see the following:

```bash
$ gpg --list-public-keys
/Users/jas/.gnupg/pubring.kbx
-----------------------------
pub   ed25519/0x97350083B861B66A 2022-02-24 [SC] [expires: 2072-02-12]
      Key fingerprint = A1D1 1351 0A1E 68CA FF6C  5798 9735 0083 B861 B66A
uid                   [ultimate] Jas Powell <jas@davepowell.net>
sub   cv25519/0xCDEC82D1091C8781 2022-02-24 [E] [expires: 2024-02-24]
sub   ed25519/0x3EABAD70AA17837B 2022-02-24 [A] [expires: 2024-02-24]
sub   ed25519/0xC94421E14BB1BF25 2022-02-24 [S] [expires: 2024-02-24]
```

And we can list the secret keys:

```bash
$ gpg --list-secret-keys
/Users/jas/.gnupg/pubring.kbx
-----------------------------
sec   ed25519/0x97350083B861B66A 2022-02-24 [SC] [expires: 2072-02-12]
      Key fingerprint = A1D1 1351 0A1E 68CA FF6C  5798 9735 0083 B861 B66A
uid                   [ultimate] Jas Powell <jas@davepowell.net>
ssb   cv25519/0xCDEC82D1091C8781 2022-02-24 [E] [expires: 2024-02-24]
ssb   ed25519/0x3EABAD70AA17837B 2022-02-24 [A] [expires: 2024-02-24]
ssb   ed25519/0xC94421E14BB1BF25 2022-02-24 [S] [expires: 2024-02-24]
```

## Export the keys from the machine

Make a location to export the keys to:

```bash
$ mkdir $HOME/keyexport
```

And first export the master secret key:

```bash
$ gpg -a --export-secret-keys A1D113510A1E68CAFF6C579897350083B861B66A > $HOME/keyexport/A1D113510A1E68CAFF6C579897350083B861B66A.sec
```

Next export the public key:

```bash
$ gpg -a --export A1D113510A1E68CAFF6C579897350083B861B66A > $HOME/keyexport/A1D113510A1E68CAFF6C579897350083B861B66A.pub
```

Export the secret sub keys:

```bash
$ gpg -a --export-secret-subkeys A1D113510A1E68CAFF6C579897350083B861B66A > $HOME/keyexport/A1D113510A1E68CAFF6C579897350083B861B66A.sub.sec
```

Also, take a copy of the revocation certificate into backup storage:

```bash
$ cp /Users/jas/.gnupg/openpgp-revocs.d/A1D113510A1E68CAFF6C579897350083B861B66A.rev $HOME/keyexport/
```

Let's check our archive:

```bash
$ ls -la $HOME/keyexport/
total 32
drwxr-xr-x   6 jas  staff   192 Feb 24 08:39 .
drwxr-xr-x+ 64 jas  staff  2048 Feb 24 08:28 ..
-rw-r--r--   1 jas  staff  1302 Feb 24 08:36 A1D113510A1E68CAFF6C579897350083B861B66A.pub
-rw-------   1 jas  staff  1269 Feb 24 08:39 A1D113510A1E68CAFF6C579897350083B861B66A.rev
-rw-r--r--   1 jas  staff  1503 Feb 24 08:33 A1D113510A1E68CAFF6C579897350083B861B66A.sec
-rw-r--r--   1 jas  staff  1467 Feb 24 08:38 A1D113510A1E68CAFF6C579897350083B861B66A.sub.sec
```

Looks good. Now we should archive this file and put it in secure offline storage:

```bash
$ tar -zcvf $HOME/keyexport.tar.gz $HOME/keyexport/*
tar: Removing leading '/' from member names
a Users/jas/keyexport/A1D113510A1E68CAFF6C579897350083B861B66A.pub
a Users/jas/keyexport/A1D113510A1E68CAFF6C579897350083B861B66A.rev
a Users/jas/keyexport/A1D113510A1E68CAFF6C579897350083B861B66A.sec
a Users/jas/keyexport/A1D113510A1E68CAFF6C579897350083B861B66A.sub.sec
```

Copy the file `$HOME/keyexport.tar.gz` onto a USB drive that you keep in a secure place.

## Detatch the Master key

Now, we need to remove the secret key (and subkeys) from `gpg`:

```bash
$ gpg --delete-secret-key A1D113510A1E68CAFF6C579897350083B861B66A

sec  ed25519/0x97350083B861B66A 2022-02-24 Jas Powell <jas@davepowell.net>

Delete this key from the keyring? (y/N) y
This is a secret key! - really delete? (y/N) y
```

Then re-import the subkeys only:

```bash
$ gpg --import $HOME/keyexport/A1D113510A1E68CAFF6C579897350083B861B66A.sub.sec
gpg: key 0x97350083B861B66A: "Jas Powell <jas@davepowell.net>" not changed
gpg: To migrate 'secring.gpg', with each smartcard, run: gpg --card-status
gpg: key 0x97350083B861B66A: secret key imported
gpg: Total number processed: 1
gpg:              unchanged: 1
gpg:       secret keys read: 1
gpg:   secret keys imported: 1
```

List the keys:

```bash
$ gpg -K
/Users/jas/.gnupg/pubring.kbx
-----------------------------
sec#  ed25519/0x97350083B861B66A 2022-02-24 [SC] [expires: 2072-02-12]
      Key fingerprint = A1D1 1351 0A1E 68CA FF6C  5798 9735 0083 B861 B66A
uid                   [ultimate] Jas Powell <jas@davepowell.net>
ssb   cv25519/0xCDEC82D1091C8781 2022-02-24 [E] [expires: 2024-02-24]
ssb   ed25519/0x3EABAD70AA17837B 2022-02-24 [A] [expires: 2024-02-24]
ssb   ed25519/0xC94421E14BB1BF25 2022-02-24 [S] [expires: 2024-02-24]
```

So, do you see above, now when we list the secret keys it says `sec#` to show us that the secret sub keys are detached from the master secret key (which is now on your backup USB)!

## Clean Up

Make sure you have copied the `$HOME/keyexport.tar.gz` file out to a USB *and tested the backup* before you delete the file. 

**NOTE** that `srm` on Mac OS and `shred` are no longer fit for purpose as secure delete tools and are useless against file system forensics. 

The most effective way to delete the files was to umount the RAM disk image you created for temporary storage of the secret key material, but you saw that on the header of this post, didn't you!?