Title: Passing Secrets with AGE Encryption
Date: 2025-03-14 10:00
Modified: 2025-03-14 10:00
Category: Tech-Recipe
Tags: linux, macos, encryption, age
Slug: passing-secrets-with-age-encryption
Author: Jas Powell
Summary: We don't use GPG any longer. But if you have to...
Status: published 
[//]: # (comment on status: published, draft, hidden, skip)

> [!NOTE]
> The environment used for this was: Linux i7 16Gb Debian 12.9

## Download a binary

A summary of the README here: https://github.com/FiloSottile/age

Download a binary, or install a version, guide on the README.

I used this:

```sh
$ curl -JLO "https://dl.filippo.io/age/v1.2.0?for=darwin/arm64"
$ tar -zxvf age-v1.2.0-darwin-arm64.tar.gz
```

## Use github keys for encryption

We will use github keys for encryption as follows:

```sh
$ echo "Hello cruel world" > helloworld.txt
$ cat helloworld.txt
Hello cruel world

$ curl https://github.com/<username>.keys | ./age -a -R - -o helloworld.txt.age helloworld.txt
cat helloworld.txt.age
-----BEGIN AGE ENCRYPTED FILE-----
YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IHNzaC1lZDI1NTE5IFRFWVQ1dyBQcGgy
MVF4dUdKZmhIc01qOEtwUXVFVmxqRnRXM3NhZXdUQWFZVnFUVUVNCmovejR3ZjlE
bk1tVkRITm9JQjVjVkcyUlVsclljV1BadSs1QkFlVDI3SlEKLS0tIEo3bUR3bU1F
MVVtcHVCRUtybjdmTjRWTmYrdWhTTlBuQXBvckY5MktrRGcKfqFRLsLgVJrV7Hp3
Inmb+6FpSrLOTmdWQUHw2MYC0bvVdlRLGfl4KVDhYF346uo3FC8=
-----END AGE ENCRYPTED FILE-----

$ ./age -d -i <secret-key> helloworld.txt.age
Hello cruel world
```

Get all keys:

```sh
$ curl -O https://github.com/<username-1>.keys
$ curl -O https://github.com/<username-2>.keys
$ curl -O https://github.com/<username-3>.keys
$ curl -O https://github.com/<username-4>.keys
```

Encrypt a text file to multiple recipients:

```sh
$ ./age -a -R <username-1>.keys -R <username-2>.keys -R <username-3>.keys -R <username-4>.keys -o the-secrets.txt.age the-secrets.txt

$ cat the-secrets.txt.age
-----BEGIN AGE ENCRYPTED FILE-----
YWdlLWVuY3J5cHRpb24ub3JnL3YxCi0+IHNzaC1yc2EgRUlURnRRCkllVE1XTm94
S1N6VHFCdEZxR25HWEc2SWNheHcwb2dFMzg1VWgwTll1UkxIT2JsQ2pjUmNPejVS
< ... snip ... >
yC3pDvCtOOHOAPQ2stlutEoIkvApZfYn+hiSXJLshkSBrdQt1VlZnu+SPsBd+669
Nh21esjpLCVZJRmJU263ySmPm+X5Uowsw440iS8/cT6M7RjDFuduJ0QluLS40q56
j/yWkIxXLaFUs/llwbTKuNxNy/XK5HDf6xiEwgFM
-----END AGE ENCRYPTED FILE-----
```

Decrypt using your private key:

```sh
$ ./age -d -i <secret-key> the-secrets.txt.age
```