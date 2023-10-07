---
title: "Dr David 'Jas' Powell"
date: 2026-03-15
subtitle: "Professional history, education, and credentials"
description: "Engineering Management & Leadership - Interim, Contract & Permanent"
comments: false
---

## Summary

Engineering leader with 25 years building and rebuilding engineering organisations - usually from a standing start, usually under hard constraint. Seven companies across regulated finance, maritime autonomy, automotive, mobile security and defence; two exits (Transitive to IBM, GuardianApp to DNSFilter). Recently architected and led delivery of an agentic-AI research platform now used weekly by 20,000 people, and designed a retrieval-augmented system that runs entirely offline on vessels at sea.

Comfortable being the first engineering hire and the one who has to make the buy-versus-build calls. Remote- and async-first by practice, not preference - most recent teams spanned Colombia to Pakistan. PhD in computational physics.

---

## Selected Outcomes

- Built and led the engineering team for a €5.7M Horizon Europe maritime autonomy consortium (11 partners) to a TRL7 demonstrator validated across **three sea trials** in Nordic and Mediterranean waters
- Took a fintech product from whiteboard to launch as founding CTO - team hired from zero, architecture set, **20,000 weekly users** today
- Core engineering and test leadership on **Rosetta**, the binary translation layer that carried millions of MacBooks from PowerPC to Intel
- Cut vehicle-to-cloud round-trip latency to **under 180ms over 4G** - good enough to run turn-by-turn navigation from a remote Android VM on a car's head unit
- Built the CI and automated fuzz-testing framework, and a white-labelled reporting engine, for a research platform serving **400+ institutional clients managing $700B+**
- Designed and deployed **Marin** - an offline RAG system (vLLM, pgvector, fine-tuned local model) answering mariners' operational questions on vessels with no connectivity

---

## Experience

### Andle Engineering Ltd - boutique consultancy, Cyprus
**Founder & Principal · May 2016 – Present**

Solo consultancy through which all engagements below were contracted. Four CTO roles, one Head of Engineering role, one senior IC engagement - typically embedded full-time for the duration, occasionally fractional and concurrent.

---

#### SafeNav Ltd - CTO & Co-Founder · Jul 2025 – Jun 2026
*Maritime autonomy spin-out · Team of 7 · Remote (London / Athens / Larnaca)*

Co-founded the company that commercialised the EU project demonstrator after concluding with the CEO that mariners would actually buy it.

- Ran the IP separation: acquired what could be acquired from consortium partners, and led a **clean-room re-architecture and rebuild** of everything that couldn't - applying the lessons from the research build rather than porting its compromises
- Architected the production stack: ROS2 Jazzy, Eclipse Zenoh, FastAPI, PostgreSQL/TimescaleDB, cross-platform across Linux, macOS and Windows
- Designed and built **Marin (Marine Intelligence)** - a RAG system on vLLM and pgvector with a fine-tuned local model, deployed to beta, running on edge nodes aboard vessels with no connectivity and no external dependencies. Built in response to watching real mariners ask real questions on the bridge underway
- Chose to build a **simulation harness rather than buy sea trials** - validated collision-avoidance behaviour against COLREGs without burning a materially large fraction of a €200K angel round on vessel time
- Completed DNVGL-CG-0264 compliance assessment and delivered a 17-item action plan; DNV Approval in Principle pending
- Raised €200K angel and ran the VC process through pre-seed conversations; the company moved to a fundraising-only footing in June 2026

#### Confidential FinTech Startup - CTO · Oct 2024 – Jul 2025
*Agentic-AI trading research for retail Forex · Team of 7 · Corporate-backed spin-off*

Brought in pre-product to turn a founder's idea into a company. Fractional alongside SafeNav until Jan 2025, then full-time.

- **Hired the entire engineering team from zero** and set the working practices, goals and review cadence
- Architected an agentic-AI system generating trading research for day traders - including the buy-versus-build boundary across the whole stack
- Made the hard call to build as a **monorepo** across a polyglot system (Python/PostgreSQL backend, Node/React frontend), and owned the CI/CD complexity that decision created
- Product launched and is used by **20,000 clients weekly**. Handed over a performing team on exit

#### SafeNav (EU Horizon Europe Project #101077026) - Head of Engineering · Sep 2022 – Jan 2025
*COLREGs-compliant collision avoidance · €4.4M EU grant / €5.7M total · 11-partner consortium · Team of 11*
*Engaged via OM Offshore Monitoring, Limassol*

- Grew the core engineering team from 6 to 11 - **hired 5**, inherited 6
- Owned architecture, planning and task management across an 11-organisation consortium of companies, SMEs and universities, coordinating engineering direction across partners with their own internal teams
- Delivered a **TRL7 technology demonstrator** taken to sea three times: two trials in Norway and Finland, one in the Mediterranean
- Ran the team across timezones from Colombia to India and Pakistan: async written updates attached to code pushes, daily stand-up in a core window, weekly and monthly consortium coordination, twice-yearly in-person partner meetings

#### GuardianApp - Senior Engineer · Jan 2021 – Aug 2022
*Smartphone cybersecurity · Acquired by DNSFilter, August 2022*

Individual contributor on a sister project to the company's main firewall and filtering product - low-level systems work by choice.

- Integrated **QEMU with the Arcan display server**, patching both to get Arcan running as a client on an existing desktop GUI rather than owning the display stack outright
- Deep C-level work across virtualisation, display server internals and window system integration
- Minor shareholder at acquisition; departed at close rather than transfer into the acquirer

#### OVO - CTO · Mar 2019 – Jun 2020
*Automotive IoT · Team of 8 plus a 5-person ODC in Kyiv*

Founded with the Munity CEO and COO to rebuild the working parts of the Munity technology for the automotive market.

- Delivered remote Android VMs rendered on in-dash vehicle head units - achieved **sub-180ms round-trip latency from vehicle to AWS Frankfurt over 4G**, low enough to run live turn-by-turn navigation in Larnaca and Tel Aviv
- **Established the Kyiv ODC from scratch** - sourcing, onboarding and running a 5-person mobile team
- Deployed to five test vehicles and demonstrated at motor shows including EcoMotion, Tel Aviv
- Two major European automotive manufacturers committed as investors; the round ended when COVID froze automotive investment in early 2020

#### Munity - CTO · May 2016 – Mar 2019
*Smartphone cybersecurity · Team of 14*

- Inherited 2 mobile developers, **built the team to 14**
- Reset the product thesis. The original brief was a hardened Android ROM for business travellers crossing hostile borders; I concluded no IT manager would buy 300 handsets and void the warranties on day one, and pivoted to a remote-desktop model instead
- Architected AOSP running on AWS Frankfurt, surfacing a full Android VM inside either an Android or iOS app - apps installed, files opened, and the VM concealable to leave only the base OS visible
- Reached **large-scale beta with 3,000 users** following an advertising campaign. Company wound down when the lead investor withdrew

---

### Albourne Partners - Software Engineer
*Cyprus · May 2012 – May 2016 · Team of 18 · Institutional hedge fund research*

Technical leadership on the platform serving **400+ institutional clients managing over $700B**, plus a social platform of 100,000 users, under Cyprus SEC financial regulation.

- Built a **PDF reporting engine from scratch**, generating custom client reports from text and graphics extracted directly from the database - white-labelled, and a genuine retention lever
- Replaced a manual build-box process with **automated CI and overnight randomised fuzz testing** across the Java codebase, with automated bug reports by email. Both systems outlasted my tenure
- Owned Jenkins pipelines across Java, Python and Unix/Linux services; set testing and observability standards for a regulated environment

### Intercollege Larnaca - Head of Department, Computer Science
*Cyprus · Jan 2009 – May 2012 · 8 staff, ~100 students*

- Brought in franchised degree packages from British universities for delivery by local faculty
- Ran hiring, performance review and development planning for the department

### Transitive - Senior Engineer
*Manchester, UK · Jul 2006 – Dec 2008 · University of Manchester spin-out, acquired by IBM*

Dynamic binary translation - the technology that shipped as **Apple's Rosetta**, enabling millions of MacBooks to run PowerPC applications on Intel silicon.

- Core engineering on the **optimisation team**, working across compiler, runtime and OS layers in C/C++
- Moved to lead a **4-person test/QA team** by choice - validating a dynamic binary translator, including bare-metal builds on IBM Power, is a genuinely hard verification problem
- Minor option holder at acquisition; stayed three months through IBM integration

### MBDA - Engineer (Jun 1999 – Aug 2001) · Apprentice Engineer (Jun 1993 – Sep 1998)
*Stevenage & Filton, UK · Defence*

Seekers and sensors, under UK MoD standards. Full apprenticeship, then part-time study to MEng alongside the engineering role.

---

## Technical

**Leadership** - Org design, hiring, 1:1 coaching, performance and development planning, OKRs, roadmap ownership, technical strategy, distributed/async teams, buy-vs-build, consortium and stakeholder management

**Architecture** - Event-driven and distributed systems, real-time and safety-critical, high-availability, API and network design, cryptography and authentication protocols

**AI/ML** - RAG architecture, vLLM, pgvector, local model fine-tuning, edge/offline inference, agentic systems, LLM-augmented engineering workflows

**Systems & Virtualisation** - Dynamic binary translation, QEMU, AOSP, display server internals (Arcan), compiler/runtime/OS-layer engineering in C/C++

**Platform & DevSecOps** - AWS, Linux, CI/CD, Jenkins, observability, OS hardening, fuzz and automated test strategy, monorepo tooling

**Languages & Runtimes** - Python, C/C++, Java, Go, Node/React, PostgreSQL/TimescaleDB, ROS2, Zenoh, AOSP/Android, Yocto, Raspberry Pi

---

## Education

**PhD, Electrical & Electronic Engineering (Nanostructure Physics)** - University of Sheffield, 2002–2006
*Elasticity, lattice dynamics and parameterisation techniques for the Tersoff potential applied to elemental and type III-V semiconductors*

**MEng, Electrical & Electronic Engineering (Artificial Intelligence)** - University of Sheffield, 1998–2002
*Automatic design of digital circuitry using genetic algorithms*

---

## Certifications

EXIN GDPR Data Protection Foundation (2018) · APMG PRINCE2 (2011)

---

## Publications

1. [Comprehensive Approaches to Enhance Maritime Wireless Networks: A Survey](https://doi.org/10.24868/11154) — Conference Proceedings of iSCSS, Nov 2024
2. [Under pressure: Control of strain, phonons and bandgap opening in rippled graphene](https://doi.org/10.1016/j.carbon.2015.04.044) — Carbon, Sep 2015
3. [Atomistic modelling of elasticity and phonons in diamond and graphene](https://doi.org/10.1109/NUSOD.2013.6633133) — 13th International Conference on Numerical Simulation of Optoelectronic Devices (NUSOD), Oct 2013
4. [Elastic and vibrational properties of group IV semiconductors in empirical potential modelling](https://dx.doi.org/10.1088/0953-8984/25/42/425801) — Journal of Physics: Condensed Matter, Sep 2013
5. [Empirical interatomic potential for the mechanical, vibrational and thermodynamic properties of semiconductors](https://dx.doi.org/10.1088/1742-6596/367/1/012015) — Journal of Physics, Jan 2012
6. [ZigBee wireless quality trials for smart meters](https://doi.org/10.1109/LAPC.2011.6114134) — Loughborough Antennas & Propagation Conference, Dec 2011
7. [TOP Biodiversity Cyprus 2010 Conference Proceedings](https://books.google.no/books?id=o-RlAgAAQBAJ) — LULU Press, Sep 2010
8. [Composition and Strain Dependence of the Piezoelectric Coefficients in Semiconductor Alloys](https://doi.org/10.1557/PROC-1017-DD04-11) — MRS Online Proceedings Library, Nov 2007
9. [Optimized Tersoff potential parameters for tetrahedrally bonded III-V semiconductors](https://doi.org/10.1103/PhysRevB.75.115202) — Physical Review B, Mar 2007
10. [Composition and strain dependence of the piezoelectric coefficients in In(x)Ga(1-x)As alloys](https://doi.org/10.1103/PhysRevB.74.245332) — Physical Review B, Dec 2006
11. [The Tersoff potential for phonons in GaAs](https://doi.org/10.1016/j.physe.2005.12.051) — Physica E: Low-dimensional Systems and Nanostructures, May 2006
12. [Elasticity, lattice dynamics and parameterisation techniques for the Tersoff potential applied to elemental and type III-V semiconductors](https://etheses.whiterose.ac.uk/15100/) — PhD Thesis, White Rose eTheses Online, Jul 2005
13. [Anisotropy of the electron energy levels in In(x)Ga(1-x)As / GaAs quantum dots with non uniform composition](https://doi.org/10.1016/j.physe.2004.08.076) — Physica E: Low-dimensional Systems and Nanostructures, Feb 2005
14. [Influence of composition on the piezoelectric effect and on the conduction band energy levels of In(x)Ga(1-x)As / GaAs quantum dots](https://doi.org/10.1063/1.1793333) — Journal of Applied Physics, Oct 2004

---

## Certifications

- **GDPR General Data Protection Foundation Certificate** — EXIN, 2018
- **PRINCE2** — APMG, 2011
