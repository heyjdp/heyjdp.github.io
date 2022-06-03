--- 
title: "\U0001f4bb Linux CLI Reminder \U0001f469\u200D\U0001f4bb \U0001f4fa \U0001f427"
date: 2022-02-10T11:00:00+02:00 
draft: false 
tags: ["tech", "linux", "commandline", "hacking"] 
author: "Jas" 
hidemeta: false 
disableShare: false
disableHLJS: false # This is the code highlighting
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
cover:
    image: "/post-img/trinity-hacking-command-line-1200-628.jpg" # image path/url
    alt: "Trinity from Matrix hacking on the Linux commandline" # alt text
#    caption: "" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: false # only hide on current single page
---

I find myself Google-ing for command-line fu a lot more than I should, here are some favourites...

<!-- more -->

## `rsync` with `ssh` 

Although this should be the default by now, really, who trusts the defaults? Manage it yourself with something like this:

```bash
rsync -avP -e "ssh -i ssh_key_file -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" /home/jas/local-dir/* remote-user@webhost.com:/home/server/www/yourdomain.com/
```

## Rainbow Shell Prompt

Put this in `.bashrc` or wherever is appropriate for your OS:

```bash
export PS1="\[$(tput bold)\]\[$(tput setaf 1)\]\u\[$(tput setaf 208)\]@\[$(tput setaf 3)\h\[$(tput setaf 2)\]:\d \[$(tput setaf 4)\]\@:\[$(tput setaf 55)\]\w\n$PROMPT_COLOR\$ \[$(tput sgr0)\]"
```

## YouTube-dl on Linux

Obtain it from here: https://github.com/ytdl-org/youtube-dl

```bash
sudo -H pip install --upgrade youtube-dl
```

Find a file then run this:

```bash
$ youtube-dl -F KIHLQzGap4Y
[youtube] KIHLQzGap4Y: Downloading webpage
[info] Available formats for KIHLQzGap4Y:
format code  extension  resolution note
249          webm       audio only tiny   52k , webm_dash container, opus @ 52k (48000Hz), 16.72MiB
250          webm       audio only tiny   69k , webm_dash container, opus @ 69k (48000Hz), 22.01MiB
140          m4a        audio only tiny  129k , m4a_dash container, mp4a.40.2@129k (44100Hz), 40.88MiB
251          webm       audio only tiny  138k , webm_dash container, opus @138k (48000Hz), 43.62MiB
160          mp4        256x144    144p   30k , mp4_dash container, avc1.4d400c@  30k, 25fps, video only, 9.55MiB
278          webm       256x144    144p   68k , webm_dash container, vp9@  68k, 25fps, video only, 21.77MiB
394          mp4        256x144    144p   73k , mp4_dash container, av01.0.00M.08@  73k, 25fps, video only, 23.27MiB
133          mp4        426x240    240p   59k , mp4_dash container, avc1.4d4015@  59k, 25fps, video only, 18.85MiB
395          mp4        426x240    240p   96k , mp4_dash container, av01.0.00M.08@  96k, 25fps, video only, 30.40MiB
242          webm       426x240    240p   99k , webm_dash container, vp9@  99k, 25fps, video only, 31.46MiB
134          mp4        640x360    360p  111k , mp4_dash container, avc1.4d401e@ 111k, 25fps, video only, 35.07MiB
396          mp4        640x360    360p  174k , mp4_dash container, av01.0.01M.08@ 174k, 25fps, video only, 55.18MiB
243          webm       640x360    360p  212k , webm_dash container, vp9@ 212k, 25fps, video only, 67.13MiB
135          mp4        854x480    480p  182k , mp4_dash container, avc1.4d401e@ 182k, 25fps, video only, 57.50MiB
397          mp4        854x480    480p  280k , mp4_dash container, av01.0.04M.08@ 280k, 25fps, video only, 88.50MiB
244          webm       854x480    480p  382k , webm_dash container, vp9@ 382k, 25fps, video only, 120.78MiB
136          mp4        1280x720   720p  298k , mp4_dash container, avc1.4d401f@ 298k, 25fps, video only, 94.19MiB
398          mp4        1280x720   720p  559k , mp4_dash container, av01.0.05M.08@ 559k, 25fps, video only, 176.66MiB
247          webm       1280x720   720p  843k , webm_dash container, vp9@ 843k, 25fps, video only, 266.30MiB
137          mp4        1920x1080  1080p 1685k , mp4_dash container, avc1.640028@1685k, 25fps, video only, 532.17MiB
399          mp4        1920x1080  1080p 1765k , mp4_dash container, av01.0.08M.08@1765k, 25fps, video only, 557.45MiB
248          webm       1920x1080  1080p 2115k , webm_dash container, vp9@2115k, 25fps, video only, 667.98MiB
18           mp4        640x360    360p  379k , avc1.42001E, 25fps, mp4a.40.2 (44100Hz), 119.91MiB (best)
```

Then we select the `audio only` (for music stuff), usually m4a:

```bash 
$ youtube-dl -f 140 KIHLQzGap4Y
```

## Convert m4a to mp3

For a single file: 

```bash 
ffmpeg -i input.m4a -c:v copy -c:a libmp3lame -q:a 4 output.mp3
```## Lorem Ipsum on the Command Line [^1]

```bash
$ curl http://metaphorpsum.com/paragraphs/20
```

And then it can be a bash alias:

```bash
loremipsum () {
  if [ "${1}" = "" ] || [ "${2}" = "" ]; then
     echo "Usage: loremipsum [paragraphs, sentences] [integer]"
  else
    curl -s http://metaphorpsum.com/"${1}"/"${2}" && printf "\n"
  fi
}
```

Brilliant lorem ipsum question and answers on stack overflow [^1].

## Generate a password on the Linux command line

Basically, do this [^2]:

```bash
cat /dev/urandom | tr -dc a-zA-Z0-9 | fold -w 18 | head -n 1
```

## Configuring Git the right way

We'll be using Git for our version control system so we're going to set it up to match our Github account. If you don't already have a Github account, make sure to register. It will come in handy for the future.

Replace my name and email address in the following steps with the ones you used for your Github account.

```bash
git config --global color.ui true
git config --global user.name "NAME"
git config --global user.email "YOU@EMAIL.com"
git config --global pull.rebase true
git config --global fetch.prune true
git config --global diff.colorMoved zebra
ssh-keygen -a 100 -t rsa -b 4096 -C "YOU@EMAIL.com" -f NAME-github-key-rsa4096
ssh-keygen -a 100 -t ed25519 -C "YOU@EMAIL.com" -f NAME-github-key-ed25519
```

The three commands rebase, prune and zebra came from this blog post called "Three Git Configurations that Should Be the Default" which is well worth your time.

The next step is to take the newly generated SSH key and add it to your Github account. You want to copy and paste the output of the following command and paste it here.

```bash
cat NAME-github-key-rsa4096.pub
cat NAME-github-key-ed25519.pub
```

Once you've done this, you can check and see if it worked:

```bash
ssh -i cat NAME-github-key-rsa4096 -T git@github.com
ssh -i cat NAME-github-key-ed25519 -T git@github.com
```

You should get a message like this:

```bash
Hi NAME! You've successfully authenticated, but GitHub does not provide shell access.
```

[^1]: *Is there something like a Lorem Ipsum generator?*, https://unix.stackexchange.com/questions/97160/is-there-something-like-a-lorem-ipsum-generator

[^2]: *How to generate a strong password on the Linux command line*, https://ostechnix.com/4-easy-ways-to-generate-a-strong-password-in-linux 

[^3]: *Three Git Configurations that S
```bash 
for f in *.m4a; do ffmpeg -i "$f" -codec:v copy -codec:a libmp3lame -q:a 2 "${f%.m4a}.mp3"; done
```

## Python3 should be the default on Debian10

Really, it has been a long time, more than a decade since Python3 
was released in 2008 and it should be the default everywhere by
now. Anyway...

```bash
$ python --version
Python 2.7.16

$ sudo update-alternatives --list python
update-alternatives: error: no alternatives for python

$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 1
update-alternatives: using /usr/bin/python2.7 to provide /usr/bin/python (python) in auto mode
$ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 2
update-alternatives: using /usr/bin/python3.4 to provide /usr/bin/python (python) in auto mode

$ sudo update-alternatives --list python
/usr/bin/python2.7.16
/usr/bin/python3.7.3

$ sudo update-alternatives --config python
There are 2 choices for the alternative python (providing /usr/bin/python).

  Selection    Path              Priority   Status
------------------------------------------------------------
* 0            /usr/bin/python3   2         auto mode
  1            /usr/bin/python2   1         manual mode
  2            /usr/bin/python3   2         manual mode

Press <enter> to keep the current choice[*], or type selection number: 0

$ python --version
Python 3.7.3
```

## Lorem Ipsum on the Command Line [^1]

```bash
$ curl http://metaphorpsum.com/paragraphs/20
```

And then it can be a bash alias:

```bash
loremipsum () {
  if [ "${1}" = "" ] || [ "${2}" = "" ]; then
     echo "Usage: loremipsum [paragraphs, sentences] [integer]"
  else
    curl -s http://metaphorpsum.com/"${1}"/"${2}" && printf "\n"
  fi
}
```

Brilliant lorem ipsum question and answers on stack overflow [^1].

## References

[^1]: *Is there something like a Lorem Ipsum generator?*, https://unix.stackexchange.com/questions/97160/is-there-something-like-a-lorem-ipsum-generator

[^2]: *How to generate a strong password on the Linux command line*, https://ostechnix.com/4-easy-ways-to-generate-a-strong-password-in-linux 

[^3]: *Three Git Configurations that Should Be the Default*, https://spin.atomicobject.com/2020/05/05/git-configurations-default/
