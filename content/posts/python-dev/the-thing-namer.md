--- 
title: "\U0001f4bb The Thing Namer \U0001f40d \U0001f469\u200D\U0001f4bb \u2728" 
date: 2021-06-02T11:00:00+02:00 
draft: false 
tags: ["tech", "python", "development"] 
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
    image: "/post-img/letraset-1200x630.jpg" # image path/url
    alt: "An old letraset transparency" # alt text
#    caption: "" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: false # only hide on current single page
---

> There are two hard problems in computer science: we have one joke, and it's not funny.
> 
> -- heyjdp

I have things that need naming. So I propose a short project to arbitrarily name projects, because why not? It's fun!

<!--more-->

So, the real quote looks like this:

> There are only two hard things in Computer Science: cache invalidation and naming things.
> 
> -- Phil Karlton

I found a blog post called [Why Is Naming Things Hard?](https://neilkakkar.com/why-is-naming-things-hard.html) and that does a far better job than I can of explaining the above quote. What I would much rather do is write a short piece of code to help me name things!

## The Thing Namer Project

I had an idea that The Thing Namer could just bolt a `NounVerb` couple together to make a fun sounding name. 

I quickly lashed some Python3 code together and came up with the following:

```python
import random

def main():
    with open('english-nouns.txt') as file:
        nouns = file.readlines()
    with open('english-verbs.txt') as file:
        verbs = file.readlines()

    noun = random.choice(nouns).rstrip().capitalize()
    verb = random.choice(verbs).rstrip().capitalize()
    
    thing_name = noun + verb
    print(f'ThingName: {thing_name}')

if __name__ == "__main__":
    main()
```

And we can see from the following output that this is working nicely...

```bash
$ python3 thing-namer.py
ThingName: BathHug

$ python3 thing-namer.py
ThingName: AfterthoughtWeep

$ python3 thing-namer.py
ThingName: WatchImplement

$ python3 thing-namer.py
ThingName: MaskScorch
```

## The Word Lists

I found some word lists in another repo that the author was using to [generate random pass phrases](https://github.com/aaronbassett/Pass-phrase), ala XKCD's [Correct Horse Battery Staple](https://xkcd.com/936/). Basically they are just plain text files with one word per line. I shall use the Python3 `.rstrip()` function to clean the lists. If you need a visual representation, make a file called `english-nouns.txt` and do this:

```txt
tub
van
apple
arm
banana
bike
bird
book
chin
clam
```

If you looked in the `pass-phrase` repo you will have noticed that there is a list of adjectives too. My tuple is now `AdjectiveNounVerb` and it is throwing some great names out:

```bash
$ python3 thing-namer.py
ThingName: ObedientWindowSting

$ python3 thing-namer.py
ThingName: ExclusiveKiteFollow

$ python3 thing-namer.py
ThingName: HarshBerryWeigh

$ python3 thing-namer.py
ThingName: CleanRakeCatalog
```

## Nouns of Agency

Alright, so because we are naming things, we don't want a verb there at the end. We want to form what is called a Noun of Agency. The suffixes "-er," "-or," and "-ar" are all used to create nouns of agency (indicating "a person or thing that performs an action") from verbs.

In practice, when the ThingNamer spits out `HarshBerryWeigh`, what I actually wanted was to name the next computer code section the `HarshBerryWeigher`. Also:

```txt
ObedientWindowSting -> ObedientWindowStinger
ExclusiveKiteFollow -> ExclusiveKiteFollower
HarshBerryWeigh -> HarshBerryWeigher
CleanRakeCatalog -> CleanRakeCataloger
```

Given my very rudimentary understanding of English, I want to replace all verbs that end in `y` with an `ier`. I want to suffix all verbs that end with and `e` with an additional `r`. And all other verbs with an `er` suffix.

```python
    if (name_v.endswith('e')):
        name_v = name_v + 'r'
    elif (name_v.endswith('y')):
        name_v = name_v[:-1] + 'ier'
    else:
        name_v = name_v + 'er'
```

I am pretty pleased with that as rough and ready rulez of engagement! I'll put the code in the GitHub in case anyone wants to pull it or whatever, but it is pretty straightforward really.

And, should I ever find the time to come back to this project and try and fix those suffix rules for the Nouns of Agency, a reference like this one will be perfect: [Suffix rules for Nouns of Agency](https://www.thefreedictionary.com/Commonly-Confused-Suffixes-er-or-ar.htm)

## The Code

If you want to give it a spin, install Python3, include wordlists of nouns, verbs and adjectives, and run this code:

```python
import argparse
import random

def read_file(filename, type, q):
    if (filename) is None:
        print('File cannot be blank')
        exit()
    with open(filename) as file:
        output = file.readlines()
    if q != True:
        print(f'Read {len(output)} {type} from {filename}')
    return output

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-n', '--nouns', dest='nouns', 
        default='english-nouns.txt', help='name of nouns file (one per line)')
    parser.add_argument('-v', '--verbs', dest='verbs', 
        default='english-verbs.txt', help='name of verbs file (one per line)')
    parser.add_argument('-a', '--adjectives', dest='adjectives', 
        default='english-adjectives.txt', help='name of adjectives file (one per line)')
    parser.add_argument('-q', default=False, action='store_true', help='be quiet')
    args = parser.parse_args()

    adjectives = read_file(args.adjectives, 'adjectives', args.q)
    nouns = read_file(args.nouns, 'nouns', args.q)
    verbs = read_file(args.verbs, 'verbs', args.q)

    name_a = random.choice(adjectives).rstrip().capitalize()
    name_n = random.choice(nouns).rstrip().capitalize()
    name_v = random.choice(verbs).rstrip().capitalize()
    
    # Super basic verb mash-er, we miss loads of rules, but we can parse manually
    if (name_v.endswith('e')):
        name_v = name_v + 'r'
    elif (name_v.endswith('y')):
        name_v = name_v[:-1] + 'ier'
    else:
        name_v = name_v + 'er'

    thing_name = name_a + name_n + name_v
    print(f'ThingName: {thing_name}')

if __name__ == "__main__":
    main()
```

## The Results

And here are some of the more fun sounding results from spinning the wheel of the ThingNamer:

```bash
$ python3 thing-namer.py -q
ThingName: ThankfulMindProgresser

$ python3 thing-namer.py -q
ThingName: VolatileEarJamer

$ python3 thing-namer.py -q
ThingName: QuixoticSuitScribbler

$ python3 thing-namer.py -q
ThingName: UptightDoctorBubbler

$ python3 thing-namer.py -q
ThingName: OrdinaryRiddleProducer

$ python3 thing-namer.py -q
ThingName: EvanescentDimeSiner

$ python3 thing-namer.py -q
ThingName: FallaciousOceanFooler

$ python3 thing-namer.py -q
ThingName: UppityStarSoother

$ python3 thing-namer.py -q
ThingName: PainstakingNailPracticer

$ python3 thing-namer.py -q
ThingName: HeavyChinExpresser

$ python3 thing-namer.py -q
ThingName: OrdinaryCoastDecider

$ python3 thing-namer.py -q
ThingName: UnadvisedCowWobbler
```

That was fun, we can find a couple of those pesky English suffix rules got broken where `VolatileEarJamer` should be `VolatileEarJammer` and also that `EvanescentDimeSiner` should be `EvanescentDimeSinner`, but for a single afternoon project, this was fine.

FIN