--- 
title: "\U0001f4bb Network Time Protocol Constraints \u23F0 \U0001f469\u200D\U0001f4bb \U0001f528" 
date: 2022-08-24T11:30:00+02:00 
draft: false 
tags: ["tech", "linux", "unix", "openbsd", "ntp", "openntpd"] 
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
    image: "/post-img/broken-clock-1200x630.jpg" # image path/url
    alt: "An old Monopoly board" # alt text
#    caption: "" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: false # only hide on current single page
---

This long post started as a quick web query (they always do...)

As I upgraded OpenBSD on my router I paid attention to the `ntpd.conf` example file and found this curious comment:

<!--more-->

```bash
17:11 root@jalapeno:/home/jas# cat /etc/examples/ntpd.conf                                                                                 
# $OpenBSD: ntpd.conf,v 1.5 2019/11/11 16:44:37 deraadt Exp $
# sample ntpd configuration file, see ntpd.conf(5)
<!--snip-->
# get the time constraint from a well-known HTTPS site
constraint from "9.9.9.9"		    # quad9 v4 without DNS
constraint from "2620:fe::fe"		# quad9 v6 without DNS
constraints from "www.google.com"	# intentionally not 8.8.8.8
```

And I wondered:

- What is/are `ntpd` Time Constraint(s)?
- What real computer problem does that actually solve?
- And why use google.com?
- Is this just another way that my online privacy is being eroded by Google?

Well, that opened a can of worms for me... silly rabbit!

## The Network Time Protocol



### How does my computer know what the time is?

We all remember that Computerphile video that should have been called "Timezones - Tom Scott's descent into madness"[^1], right?

Well... here is a rabbit hole for you [^1] :) 

Stuff [^2]

Things [^3]

RFCs [^4] [^5] [^6] [^7] [^8] [^9] [^10] [^11] [^12] yikes

## References

[^1]: **The Problem with Time & Timezones - Computerphile**, https://www.youtube.com/watch?v=-5wpm-gesOY 

[^1]: **OpenNTPD** https://www.openntpd.org/ 
[^2]: **NTP configuration best practices** https://docs.cloudera.com/cdp-private-cloud-base/7.1.3/troubleshooting-kudu/topics/kudu-ntp-configuration-best-practices.html
[^3]: **What is NTP?** http://www.ntp.org/ntpfaq/NTP-s-def.htm 
[^4]: **RFC5905, Network Time Protocol Version 4: Protocol and Algorithms Specification** https://datatracker.ietf.org/doc/html/rfc5905 
[^5]: **RFC4330, Simple Network Time Protocol (SNTP) Version 4 for IPv4, IPv6 and OSI** https://datatracker.ietf.org/doc/html/rfc4330 
[^6]: **RFC2030, Simple Network Time Protocol (SNTP) Version 4 for IPv4, IPv6 and OSI** https://datatracker.ietf.org/doc/html/rfc2030 
[^7]: **RFC1769, Simple Network Time Protocol (SNTP)** https://datatracker.ietf.org/doc/html/rfc1769
[^8]: **RFC1361, Simple Network Time Protocol (SNTP)** https://datatracker.ietf.org/doc/html/rfc1361
[^9]: **RFC1305, Network Time Protocol (Version 3) Specification, Implementation and Analysis** https://datatracker.ietf.org/doc/html/rfc1305 
[^10]: **RFC1119, Network Time Protocol (Version 2) Specification and Implementation** https://datatracker.ietf.org/doc/html/rfc1119 
[^11]: **RFC1059, Network Time Protocol (Version 1) Specification and Implementation** https://datatracker.ietf.org/doc/html/rfc1059 
[^12]: **RFC958, Network Time Protocol (NTP)** https://datatracker.ietf.org/doc/html/rfc958 

[^13]: **Calomel NTP Setup** https://calomel.org/ntpd.html
[^14]: **StratumOneTimeServers** https://support.ntp.org/bin/view/Servers/StratumOneTimeServers 
[^15]: **dns-lookup/pool.ntp.org** https://www.robtex.com/dns-lookup/pool.ntp.org 
[^16]: **Configure NTP for Use in the NTP Pool** https://www.digitalocean.com/community/tutorials/how-to-configure-ntp-for-use-in-the-ntp-pool-project-on-ubuntu-16-04 
[^17]: **Hideous YouTube 'Tutorial' for OpenBSD NTP - DO NOT WATCH**, https://www.youtube.com/watch?v=UHmxZqSL-9c 

