---
title: "\U0001f4bb Linear Feedback Shift Register \u26D3 \u2728 \U0001f469\u200D\U0001f4bb"
date: 2020-02-17T11:00:00+02:00
draft: false
tags: ["tech", "random numbers", "development"] 
hidemeta: false
disableShare: false
disableHLJS: false # This is the code highlighting
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
katex: true
cover:
    image: "/post-img/linear-feedback-shift-register-1200x628.jpg" # image path/url
    alt: "A linear feedback shift register" # alt text
#    caption: "" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: false # only hide on current single page
---

How did I get started in technology? Great question, let's explore...

<!--more-->

> "I suppose it is tempting, if the only tool you have is a hammer, to treat everything as if it were a nail." -- *Abraham Maslow, 1966*

It was in late 1993 when I first got my ass kicked by a maths puzzle. What was this feeling? How to describe this new sensation? I had literally never come across anything I couldn't just "figure out" before. But this was new...

To the soundtrack of Cannonball by The Breeders [^1], I flipped the pages of my 2nd edition The Art of Electronics (TAOE) by Horowitz and Hill [^2]. The leaden scent of vaporised solder was in the air from a half-populated breadboard in my little electronics lab in Filton, Bristol. I was taking a reference library break. Next to my lukewarm, milky coffee was a brown envelope which was covered in a sketch, a block diagram of a proposed circuitry project. Later, after my lunch break, I would be fusing macrocells in the CPLD that I was planning to add to my circuit design. 

First, though I needed something to think about over my lunch. I was just checking in with exactly what was involved in designing a Linear Feedback Shift Register (LFSR). The LFSR was the component required to generate the pseudo-random noise that I would XOR into my digital telemetry signal to render it unreadable by anyone that didn't have the same circuitry design as me. 

I was feeling pretty smug about my little life as I read from TAOE:

## Pseudorandom bit sequences and noise generation

### Digital-noise generation

*An interesting blend of digital and analog techniques is embodied in the subject of pseudo-random bit sequences (PRBSs). It turns out to be remarkably easy to generate sequences of bits (or words) that have good randomness properties, i.e., a sequence that has the same sort of probability and correlation properties as an ideal coin-flipping machine. Because these sequences are generated by standard deterministic logic elements (shift registers, to be exact), the bit sequences generated are in fact predictable and repeatable, although any portion of such a sequence looks for all the world just like a random string of 0s and 1s.*

### Feedback shift register sequences

*The most popular (and the simplest) PRBS generator is the linear feedback shift register (LFSR, Figure 13.111). A shift register of length m bits is clocked at some fixed rate, \\(f_0\\) . An exclusive-OR gate generates the serial input signal from the exclusive-OR combination of the \\(n\\)th bit and the last (\\(m\\)th) bit of the shift register. Such a circuit goes through a set of states (defined by the set of bits in the register after each clock pulse), eventually repeating itself after \\(K\\) clock pulses; i.e., it is cyclic with period \\(K\\).*

*The maximum number of conceivable states of an \\(m\\)-bit register is \\(K = 2 m\\) , i.e., the number of binary combinations of \\(m\\) bits. However, the state of all 0s would get "stuck" in this circuit, because the exclusive-OR would regenerate a 0 at the input. Thus the maximum-length sequence you can possibly generate with this scheme is \\(2 m −1\\). It turns out that you can make such "maximal-length shift-register sequences" if \\(m\\) and \\(n\\) are chosen correctly, and the resultant bit sequence is pseudo-random.\\(^{136}\\)*

THERE! That little footnote, number \\(^{136}\\). Let's check what it says: 

> 136. The criterion for maximal length is that the polynomial \\(1+x^n +x^m\\) be
>      irreducible and prime over the Galois field GF(2).

Oh, wow! I had no idea what that meant. What is a Galois field? And how could that polynomial be prime? And what does \\(GF(2)\\) even mean? 

My first ass kicking occurred when I asked my line manager about Galois. He promptly giggled at my lack of nouse and corrected my pronunciations: "[Gal-Wa](https://en.wikipedia.org/wiki/%C3%89variste_Galois) dear, he was French" [^3]. I was advised to head over to the library and check the theoretical maths section. There was no Internet in those days, so I had to physically march out of the office, totally at a loss as to what a Galois Field [^4] GF(2) was or how to work out what was prime in GF(2). 

And that started a 30 year long search for all things pseudo-random, encrypted and mathematically difficult. That search has taken me to some interesting places, including:

- a 10-year trip to the University of Sheffield for a sprinkling of degree certificates (including a PhD) in Electronic Engineering and Computing 
- a 10-year trip to a Mediterranean island to build a family life and a home
- various roles in executive leadership and team leadership
- trips to many of the best libraries of the world
- various roles in network security, cryptography and secure systems design/development
- advanced compiler design, development and test
- various roles in rapid prototyping (hardware, software, cloud computing) 
- experience working with/for (name dropping time...) IBM, Apple, Cisco, RedHat, Sun/Oracle on hardware such as x86/64, MIPS, Sparc8/9, Cell Engine, ARM/aarch64 and PowerPC

And here we are...

## Contact

- dave@davepowell.net
- https://heyjdp.github.io

## References

[^1]: "Cannonball" - The Breeders, https://youtu.be/fxvkI9MTQw4 
[^2]: The Art of Electronics, https://artofelectronics.net/ 
[^3]: Évariste Galois, https://en.wikipedia.org/wiki/%C3%89variste_Galois 
[^4]: Galois Field, https://en.wikipedia.org/wiki/Finite_field 
