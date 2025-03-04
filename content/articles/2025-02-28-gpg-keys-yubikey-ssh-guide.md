Title: GPG Keys for Yubikey and SSH Guide
Date: 2025-03-04 10:00
Modified: 2025-03-04 10:00
Category: Tech-Recipe
Tags: linux, macos, encryption, gpg
Slug: gpg-keys-yubikey-ssh-guide
Author: Jas Powell
Summary: We don't use GPG any longer. But if you have to...
Status: published 
[//]: # (comment on status: published, draft, hidden, skip)

> [!NOTE]
> The environment used for this was: Linux i7 16Gb Debian 12.9

## Stop GPG using GUI to prompt for passphrase

Do this:

```sh
sudo apt install pinentry-tty
sudo update-alternatives --set pinentry /usr/bin/pinentry-tty
```

## GPG Defaults

Use this file in `~/.gnupg/gpg.conf`:

```sh
# https://github.com/drduh/config/blob/master/gpg.conf
# https://www.gnupg.org/documentation/manuals/gnupg/GPG-Options.html
# 'gpg --version' to get capabilities
# Use AES256, 192, or 128 as cipher
personal-cipher-preferences AES256 AES192 AES
# Use SHA512, 384, or 256 as digest
personal-digest-preferences SHA512 SHA384 SHA256
# Use ZLIB, BZIP2, ZIP, or no compression
personal-compress-preferences ZLIB BZIP2 ZIP Uncompressed
# Default preferences for new keys
default-preference-list SHA512 SHA384 SHA256 AES256 AES192 AES ZLIB BZIP2 ZIP Uncompressed
# SHA512 as digest to sign keys
cert-digest-algo SHA512
# SHA512 as digest for symmetric ops
s2k-digest-algo SHA512
# AES256 as cipher for symmetric ops
s2k-cipher-algo AES256
# UTF-8 support for compatibility
charset utf-8
# No comments in messages
no-comments
# No version in output
no-emit-version
# Disable banner
no-greeting
# Long key id format
keyid-format 0xlong
# Display UID validity
list-options show-uid-validity
verify-options show-uid-validity
# Display all keys and their fingerprints
with-fingerprint
# Display key origins and updates
#with-key-origin
# Cross-certify subkeys are present and valid
require-cross-certification
# Enforce memory locking to avoid accidentally swapping GPG memory to disk
require-secmem
# Disable caching of passphrase for symmetrical ops
no-symkey-cache
# Output ASCII instead of binary
armor
# Enable smartcard
use-agent
# Disable recipient key ID in messages (breaks Mailvelope)
throw-keyids
# Default key ID to use (helpful with throw-keyids)
#default-key 0xFF00000000000001
#trusted-key 0xFF00000000000001
# Group recipient keys (preferred ID last)
#group keygroup = 0xFF00000000000003 0xFF00000000000002 0xFF00000000000001
# Keyserver URL
#keyserver hkps://keys.openpgp.org
#keyserver hkps://keys.mailvelope.com
#keyserver hkps://keyserver.ubuntu.com:443
#keyserver hkps://pgpkeys.eu
#keyserver hkps://pgp.circl.lu
#keyserver hkp://zkaan2xfbuxia2wpf7ofnkbz6r5zdbbvxbunvp5g2iebopbfc4iqmbad.onion
# Keyserver proxy
#keyserver-options http-proxy=http://127.0.0.1:8118
#keyserver-options http-proxy=socks5-hostname://127.0.0.1:9050
# Enable key retrieval using WKD and DANE
#auto-key-locate wkd,dane,local
#auto-key-retrieve
# Trust delegation mechanism
#trust-model tofu+pgp
# Show expired subkeys
#list-options show-unusable-subkeys
# Verbose output
#verbose
```

## Generate Master Key

Do this:

```sh
gpg --quick-generate-key \
    'Your Name <your.email@example.com> (optional comment)' \
    ed25519 cert never
```

You will see an output like this:

```sh
gpg: directory '/home/jas/.gnupg/openpgp-revocs.d' created
gpg: revocation certificate stored as '/home/jas/.gnupg/openpgp-revocs.d/03A99DA4A0BA3F8EDBCD7ECF9A2A84EDC48BBCFC.rev'
public and secret key created and signed.

pub   ed25519/0x9A2A84EDC48BBCFC 2025-03-04 [C]
      Key fingerprint = 03A9 9DA4 A0BA 3F8E DBCD  7ECF 9A2A 84ED C48B BCFC
uid                              Jas Powell <jas@example.com>
```

Giong forward, we are interested in this number, the key fingerprint: `03A99DA4A0BA3F8EDBCD7ECF9A2A84EDC48BBCFC`

## Add Subkeys

Now add subkeys for signing, encryption, and authentication. These will have expiration times to allow for key rotation. For example, using a one year expiration time:

```sh
gpg --quick-add-key 03A99DA4A0BA3F8EDBCD7ECF9A2A84EDC48BBCFC ed25519 sign 1y
gpg --quick-add-key 03A99DA4A0BA3F8EDBCD7ECF9A2A84EDC48BBCFC cv25519 encr 1y
gpg --quick-add-key 03A99DA4A0BA3F8EDBCD7ECF9A2A84EDC48BBCFC ed25519 auth 1y
```

## Verify the Keys

Now check you have the keys with command: `gpg -K`

```sh
gpg -K
/home/jas/.gnupg/pubring.kbx
----------------------------
sec   ed25519/0x9A2A84EDC48BBCFC 2025-03-04 [C]
      Key fingerprint = 03A9 9DA4 A0BA 3F8E DBCD  7ECF 9A2A 84ED C48B BCFC
uid                   [ultimate] Jas Powell <jas@example.com>
ssb   ed25519/0xB6DFDCDABFB9E3CF 2025-03-04 [S] [expires: 2026-03-04]
ssb   cv25519/0x6A481E53769ECDF3 2025-03-04 [E] [expires: 2026-03-04]
ssb   ed25519/0x86EB33B0EF885886 2025-03-04 [A] [expires: 2026-03-04]
```

## Export Master Keys

```sh
gpg --export-secret-keys 03A99DA4A0BA3F8EDBCD7ECF9A2A84EDC48BBCFC > jas@example.com.private.gpgkey
gpg --export 03A99DA4A0BA3F8EDBCD7ECF9A2A84EDC48BBCFC > jas@example.com.public.gpgkey
cp /home/jas/.gnupg/openpgp-revocs.d/03A99DA4A0BA3F8EDBCD7ECF9A2A84EDC48BBCFC.rev jas@example.com.revocs.gpgkey
```

Don't lose these three files, these are the master keys for the laptop. Keep them in a sock drawer, in case you need to cut new subkeys after expiry.

## Detatch Master Signing Key from the Master

```sh
gpg --export-secret-subkeys jas@example.com > jas@example.com.private.gpgsubkeys
gpg --delete-secret-key jas@example.com
gpg --import jas@example.com.private.gpgsubkeys
```

Next time you need to re-install your laptop, use the command:

```sh
gpg --import jas@example.com.private.gpgsubkeys
```

## Key Check

And now we have a detatched signing key, we can check with: `gpg -K`

```sh
gpg -K
/home/jas/.gnupg/pubring.kbx
----------------------------
sec#  ed25519/0x9A2A84EDC48BBCFC 2025-03-04 [C]
      Key fingerprint = 03A9 9DA4 A0BA 3F8E DBCD  7ECF 9A2A 84ED C48B BCFC
uid                   [ultimate] Jas Powell <jas@example.com>
ssb   ed25519/0xB6DFDCDABFB9E3CF 2025-03-04 [S] [expires: 2026-03-04]
ssb   cv25519/0x6A481E53769ECDF3 2025-03-04 [E] [expires: 2026-03-04]
ssb   ed25519/0x86EB33B0EF885886 2025-03-04 [A] [expires: 2026-03-04]
```

Notice the `sec#` <- this indicates that the signing key is detached, and using the subkey.

The associated public keys are listed:

```sh
gpg -k
/home/jas/.gnupg/pubring.kbx
----------------------------
pub   ed25519/0x9A2A84EDC48BBCFC 2025-03-04 [C]
      Key fingerprint = 03A9 9DA4 A0BA 3F8E DBCD  7ECF 9A2A 84ED C48B BCFC
uid                   [ultimate] Jas Powell <jas@example.com>
sub   ed25519/0xB6DFDCDABFB9E3CF 2025-03-04 [S] [expires: 2026-03-04]
sub   cv25519/0x6A481E53769ECDF3 2025-03-04 [E] [expires: 2026-03-04]
sub   ed25519/0x86EB33B0EF885886 2025-03-04 [A] [expires: 2026-03-04]
```

## Caution

A word of advice though, all of this is security theatre. Even though we set up our algorithms, I can still see this:

```sh
gpg --edit-key 03A99DA4A0BA3F8EDBCD7ECF9A2A84EDC48BBCFC
Secret subkeys are available.

pub  ed25519/0x9A2A84EDC48BBCFC
     created: 2025-03-04  expires: never       usage: C
     trust: ultimate      validity: ultimate
ssb  ed25519/0xB6DFDCDABFB9E3CF
     created: 2025-03-04  expires: 2026-03-04  usage: S
ssb  cv25519/0x6A481E53769ECDF3
     created: 2025-03-04  expires: 2026-03-04  usage: E
ssb  ed25519/0x86EB33B0EF885886
     created: 2025-03-04  expires: 2026-03-04  usage: A
[ultimate] (1). Jas Powell <jas@example.com>

gpg> showpref
[ultimate] (1). Jas Powell <jas@example.com>
     Cipher: AES256, AES192, AES, 3DES
     AEAD:
     Digest: SHA512, SHA384, SHA256, SHA1
     Compression: ZLIB, BZIP2, ZIP, Uncompressed
     Features: MDC, AEAD, Keyserver no-modify

gpg> quit
```

I have no idea what SHA1 and 3DES are doing on that list. In 2025. GPG is broken. 
