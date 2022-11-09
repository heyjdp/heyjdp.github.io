--- 
title: "\U0001f4bb MacOS installer hung with 'Waiting for other installations to complete' \U0001f469\u200D\U0001f4bb \U0001f52e \U0001f34f" 
date: 2022-11-09T10:00:00+02:00 
draft: false 
tags: ["tech", "macos", "tools"] 
hidemeta: false 
disableShare: false
disableHLJS: false # This is the code highlighting
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
cover:
    image: "/post-img/install-locked-macos-1200x630.jpg" # image path/url
    alt: "A hung MacoS installer" # alt text
#    caption: "" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: false # only hide on current single page
---

For reasons I needed to test a set of `osquery` rules lately, so I downloaded the official package from https://osquery.io and set about running the installer. For some reason the installation got stuck at a message 'Waiting for other installation to complete'. The installer hangs for a long time, so I explored my options to unblock the installer.

<!--more-->

## Open the ‘Force Quit’ window

One of the first options you should try is to force quit the installation and try again. This should be no issue because the installation hasn’t actually started, so to interrupt it will not cause any harm whatsoever.

![A hung installer on MacOS](/post-img/install-locked-macos-1.jpg)

Force quit an app on MacOS is relatively simple an requires you to press a key combination on your keyboard: `Option+Command+Escape`.

![The force quit dialogue on MacOS](/post-img/install-locked-macos-2.jpg)

Select the installer application and choose to 'Force Quit' it. You will be prompted with the message: Do you want to force "Installer" to quit? You will lose any unsaved changes. And here you must click 'Force Quit'.

## Manually remove the installation lock

Remove the installation lock via Terminal[^2] on your Mac has high chances of succes as well. There is a big likelihood that the previous installation has failed, but the lock was not removed. The reason could be that the previous installation failed because your Mac ran out of battery and had to shut down in the middle of the installation process. But other reasons exist as well, including an application which starts during the bootup and tries to install an app on your device.

Here are the steps to follow to manually remove the installer lock:

1. Open Terminal
2. Paste the following command: `sudo rm /private/var/db/mds/system/mds.install.lock`
3. Reboot your computer, or enter this command instead: `sudo killall -1 installd`

## Boot your Mac in Safe Mode

Booting your Mac in Safe Mode is your final option[^1]. Triggering the Safe Mode option depends on your Mac: the Intel or Apple Silicon chips will have another process to follow.

### Apple 'chip' silicon

1. Shut down your Mac.
2. Turn on your Mac and continue to press and hold the power button until you see the startup options window.
3. Select your startup disk, then press and hold the Shift key while clicking "Continue in Safe Mode."
4. Log in to your Mac. You might be asked to log in again.

### Intel processor

1. Turn on or restart your Mac, then immediately press and hold the Shift key as your Mac starts up.
2. Release the key when you see the login window, then log in to your Mac. 
3. You might be asked to log in again. On either the first or second login window, you should see ”Safe Boot” in the upper-right corner of the window.

## References

[^1]: https://support.apple.com/en-gb/guide/mac-help/mh21245/mac, Booting MacOS in Safe Mode
[^2]: https://thomas.vanhoutte.be/miniblog/mac-installation-stuck-waiting-for-other-installations-to-complete/, Commandline to remove install lock from MacOS
