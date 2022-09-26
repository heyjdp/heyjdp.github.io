--- 
title: "\U0001f4bc Resume in JSON Format \U0001f469\u200D\U0001f4bc \U0001f4cb \U0001f4ce" 
date: 2022-03-18T14:00:00+02:00 
draft: false 
tags: ["tech", "office", "resume", "JSON"] 
hidemeta: false 
disableShare: false
disableHLJS: false # This is the code highlighting
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
cover:
    image: "/post-img/resume-1200x628.jpg" # image path/url
    alt: "A picture of aq resume" # alt text
#    caption: "" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: false # only hide on current single page
---

This is worth sharing: Thomas Davies (jsonresume.org) has made a online resume host and formatter, so long as your resume is in JSON format. Let's check it out...

<!--more-->

This tool, [jsonresume](https://jsonresume.org/getting-started/) look quite nifty. It takes a JSON blob and turns it into a well formatted resume that you can share on the web:

```json
{
  "basics": {
    "name": "Dr. Dave Powell",
    "label": "Experienced team leader, manager and mentor with a sleeves-up attitude to design and development",
    "image": "https://avatars0.githubusercontent.com/u/100204215?s=460&v=4",
    "summary": "Enabling tech start-ups to scale their seed ideas to mass market products. Serious about building technology teams that innovate and win.  I've worked mostly at startups so I am used to wearing many hats. I have a strong background in hands-on software and firmware engineering, security and cryptography, dev-ops, test and system architecture.",
    "website": "https://heyjdp.github.io",
    "email": "dave@davepowell.net",
    "phone": "+357 96 431 656",
    "location": {
      "city": "Larnaca",
      "countryCode": "CY"
    }
  }
}
```

The exact JSON schema is available at: [https://jsonresume.org/schema/](https://jsonresume.org/schema/)

Here is an example of the output from my resume file: [https://registry.jsonresume.org/heyjdp?theme=kendall](https://registry.jsonresume.org/heyjdp?theme=kendall)

![Example output of the JSON Resume fomatter with theme Kendall](/post-img/dave-powell-resume-from-json-1200x575.jpg)

There are many themes available too, you just need to [change the URL to change theme](https://jsonresume.org/themes/), which is nice! Also there is a QR code generator. 

I did have some challenges getting the `node` application on the command line to export a PDF file for me. But my thoughts on `node` and `npm` and the dependency hell are well known, we don't need to get into that all over again.

If you would like to play or find out more, the gihub is available from Thomas Davies here: [https://github.com/jsonresume](https://github.com/jsonresume)

My personal resume is loaded into a Github Gist here: [https://gist.github.com/heyjdp/](https://gist.github.com/heyjdp/) - make sure that you name your Gist `resume.json` and it is a public Gist, and then you can great your resume by going to URL: [https://registry.jsonresume.org/heyjdp](https://registry.jsonresume.org/heyjdp)
