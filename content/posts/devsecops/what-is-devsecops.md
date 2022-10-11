--- 
title: "\U0001f4bb What is DevSecOps? \U0001f510 \U0001f9f0 \U0001f4bb" 
date: 2022-09-11T10:30:00+02:00 
draft: false 
tags: ["tech", "cicd", "devsecops", "devops", "development"] 
hidemeta: false 
disableShare: false
disableHLJS: false # This is the code highlighting
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
cover:
    image: "/post-img/devsecops-1200x628.jpg" # image path/url
    alt: "The functions of the DevSecOps team" # alt text
#    caption: "" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: false # only hide on current single page
---

What is DevSecOps, and how is it different to the more traditional DevOps team you are used to working with?

<!--more-->

##  What is DevSecOps?

DevSecOps (short for development, security, and operations) is a development practice that integrates security initiatives at every stage of the software development lifecycle to deliver robust and secure applications.

DevSecOps infuses security into the continuous integration and continuous delivery (CI/CD) pipeline, allowing development teams to address some of today’s most pressing security challenges at DevOps speed.

Historically, security considerations and practices were often introduced late in the development lifecycle. However, with the rise of more sophisticated cybersecurity attacks, and development teams shifting to shorter, more frequent iterations on applications, DevSecOps is now becoming a go-to practice for ensuring applications are secure in this modern development ecosystem.


## What are the Benefits of DevSecOps?

Security is top of mind for every organization today. Fortunately, DevSecOp’s emphasis on incorporating security at every stage is proving to be a more secure approach to development while meeting the velocity of today’s rapid release cycle.

The DevSecOps approach brings with it specific benefits:

### Enhanced Application Security
DevSecOps embeds a proactive approach to mitigate cybersecurity threats early in the development lifecycle. This means that development teams will rely on automated security tools to test code on the fly, performing security audits without slowing development cycles.

DevOps teams will review, audit, test, scan, and debug code at various stages of the development process to ensure the application is passing critical security checkpoints. When security vulnerabilities are exposed, application security and development teams will work collaboratively on solutions at the code level to address the problem.

### Cross-team ownership
DevSecOps brings development teams and application security teams together early in the development process, building a collaborative cross-team approach. Rather than siloed, disparate operations that stifle innovation and even lead to division among business units, DevSecOps empowers teams to get on the same page early, leading to cross-team buy-in, and more efficient team collaboration.

### Streamline Application Delivery
Embed security earlier and often the development lifecycle, automate as many security processes as possible and streamline reporting all enhance security and enables compliance teams, ensuring that security practices embolden fast development cycles.

### Limit Security Vulnerabilities
Leverage automation to identify, manage, and patch common vulnerabilities and exposures (CVE). Use pre-built scanning solutions early and often to scan any prebuilt container images in the build pipeline for CVEs. Introduce security measures that not only mitigate risk but also provide insight to teams so that teams can remediate quickly when vulnerabilities are discovered.

One of the strongest benefits of DevSecOps is it creates a streamlined agile development process - an approach that if done correctly can greatly limit security vulnerabilities. Many of the cybersecurity testing processes, tasks, and services integrate quite easily with the automated services found in an application development or operations team.

## How does DevSecOps Work?

We want to design to provide development teams with the full security stack. This is achieved by establishing ongoing collaboration between development, release management (also known as operations), and the organization's security team and emphasizing this collaboration along each stage of the CI/CD Pipeline. 

The CI/DI Pipeline is broken into six stages known as Code, Build, Store, Prep, Deploy and Run.

### Code 
The first step to a development approach that aligns with DevSecOps is to code in segments that are both secured and trusted. Here, VMware Tanzu® provides tools that perform regular updates for these born-secure building blocks to better protect your data and apps from day one.

### Build 
To take code and deliver comprehensive container images that contain a core OS, application dependencies and other run-times services, requires a secure process. VMware Tanzu Build Service™ manages this securely and provides run-time dependencies scans to enhance security allowing DevSecOps teams to develop securely with agility.

### Store
Any off-the-shelf technology stack needs to be considered a risk in today’s ever-evolving cybersecurity landscape. To this point, each off-the-shelf app or back-end service should be continually checked. Fortunately, with VMware, developers can pull opinionated dependencies securely with VMware Tanzu and scan for vulnerabilities in the container image with VMware Carbon Black Cloud Container™.

### Prep
Before deployment, organizations need to ensure their application complies with security policies. To achieve this, VMware Tanzu and Carbon Black Cloud Container can validate configurations against the organization’s security policies before entering subsequent stages of the development cycle. These configurations define how the workload should run, not only providing key insight into potential vulnerabilities but also setting subsequent stages of the CI/CD pipeline up for a successful deployment.

### Deploy 
Scans delivered in previous steps give organizations a comprehensive understanding of the application’s security strength. Here, vulnerabilities or misconfigurations in the development process that has been identified are clearly presented allowing organizations to fix issues and define stronger security standards to promote a stronger security posture.

### Run
As deployments run, SecOps teams can leverage active deployment analytics, monitoring and automation to ensure continuous compliance while also mitigating the risk of vulnerabilities that surface following deployment.
