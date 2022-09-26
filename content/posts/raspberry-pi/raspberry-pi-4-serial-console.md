--- 
title: "\U0001f4bb Raspberry Pi 4 Serial Console \U0001f353 \U0001f967 \U0001f469\u200D\U0001f4bb" 
date: 2020-04-19T11:00:00+02:00 
draft: false 
tags: ["tech", "linux", "raspberry-pi", "development", "hardware"] 
hidemeta: false 
disableShare: false
disableHLJS: false # This is the code highlighting
hideSummary: false
searchHidden: true
ShowReadingTime: true
ShowBreadCrumbs: true
ShowPostNavLinks: true
cover:
    image: "/post-img/raspi-power-serial-header-1200-628.jpg" # image path/url
    alt: "Raspberry Pi header with power wires" # alt text
#    caption: "" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: false # only hide on current single page
---

Raspberry Pi has been through a few revisions now, and the data available on the www tends to get stale very fast. This is the **right** way of connecting to a Raspberry Pi 4 via a serial consoles.

<!-- more -->

## Which GPIO pins are used for the serial console?

As can be seen in the image above and the cartoon here, the `TX` (PIN8) and `RX` (PIN10) pins for the serial port are next to the `5V` power (PIN2) and `GND` (PIN6) pins on the top left. If we type `pinout` into the Ras Pi 4 then it will make the following cute terminal drawing for us:

```bash
pi@raspberrypi:~$ pinout
,--------------------------------.
| oooooooooooooooooooo J8   +======
| 1ooooooooooooooooooo  PoE |   Net
|  Wi                    oo +======
|  Fi  Pi Model 4B  V1.2 oo      |
|        ,----.               +====
| |D|    |SoC |               |USB3
| |S|    |    |               +====
| |I|    `----'                  |
|                   |C|       +====
|                   |S|       |USB2
| pwr   |HD|   |HD| |I||A|    +====
`-| |---|MI|---|MI|----|V|-------'

Revision           : c03112
SoC                : BCM2711
RAM                : 4096Mb
Storage            : MicroSD
USB ports          : 4 (excluding power)
Ethernet ports     : 1
Wi-fi              : True
Bluetooth          : True
Camera ports (CSI) : 1
Display ports (DSI): 1

J8:
   3V3  (1) (2)  5V    
 GPIO2  (3) (4)  5V    
 GPIO3  (5) (6)  GND   
 GPIO4  (7) (8)  GPIO14
   GND  (9) (10) GPIO15
GPIO17 (11) (12) GPIO18
GPIO27 (13) (14) GND   
GPIO22 (15) (16) GPIO23
   3V3 (17) (18) GPIO24
GPIO10 (19) (20) GND   
 GPIO9 (21) (22) GPIO25
GPIO11 (23) (24) GPIO8 
   GND (25) (26) GPIO7 
 GPIO0 (27) (28) GPIO1 
 GPIO5 (29) (30) GND   
 GPIO6 (31) (32) GPIO12
GPIO13 (33) (34) GND   
GPIO19 (35) (36) GPIO16
GPIO26 (37) (38) GPIO20
   GND (39) (40) GPIO21

For further information, please refer to https://pinout.xyz/
```

## Notes

0. Make sure that you have booted the Raspbian install once and manually enabled the serial port [^1]:
    ```bash
    pi@raspberrypi:~$ sudo raspi-config
    ```
    then choose `5. Interface options` >> `Serial` >> `Would like a login shell to be accessible over serial` >> `YES`. Then select `Finish` and reboot the Raspberry Pi 4 device.
    ```bash
    pi@raspberrypi:~$ sudo reboot
    ```
    The Raspberry Pi 4 has a number of UART devices available on the GPIO pins, the above seems to be the simplest way to just get a terminal over serial [^2].

1. Find the serial device on the Linux box [^3]:
    ```bash
    dave@iceberg:Mon Nov 16 06:08 PM:~
    $ dmesg | egrep --color 'serial|ttyS|ttyU'
    [46683.319955] usbcore: registered new interface driver usbserial_generic
    [46683.319966] usbserial: USB Serial support registered for generic
    [46683.321966] usbserial: USB Serial support registered for pl2303
    [46683.322620] usb 1-7: pl2303 converter now attached to ttyUSB0
    ```

2. Check device permissions and add the user to the dialout group [^4]:
    ```bash
    dave@iceberg:Mon Nov 16 07:11 PM:~
    $ ls -la /dev/ttyUSB0
    $ sudo chmod 666 /dev/ttyUSB0
    $ sudo adduser ${USER} dialout
    ```

3. Use `minicom` [^5]:
    ```bash
    dave@iceberg:Mon Nov 16 07:58 PM:~
    $ sudo minicom -b 115200 -D /dev/ttyUSB0
    ```
    and after you have the Minicom window open, then check the hardware flow control is set to **off** (`CTRL-A` + `Z` >> `O` >> `Serial port setup` >> `F` >> `Hardware Flow Control: No` >> `ESC`) And press enter a few times and you should see the prompt
    ```bash
    Raspbian GNU/Linux 10 raspberrypi ttyS0 
    
    raspberrypi login: 
    ```
    Congratulations, enjoy your serial port!

4. If `minicom` is too clunky (yeah, I know), then try `tio` - it is supposed to be self configuring [^6]. It works well actually...
    ```bash
    dave@iceberg:Mon Nov 16 08:09 PM:~
    $ sudo tio /dev/ttyUSB0
    [tio 20:09:35] tio v1.32
    [tio 20:09:35] Press ctrl-t q to quit
    [tio 20:09:35] Connected

    pi@raspberrypi:~$ 
    ```
    you can ask `tio` for the configuration with `CTRL-C` + `c`:
    ```bash
    [tio 20:29:03] Configuration:
    [tio 20:29:03]  TTY device: /dev/ttyUSB0
    [tio 20:29:03]  Baudrate: 115200
    [tio 20:29:03]  Databits: 8
    [tio 20:29:03]  Flow: none
    [tio 20:29:03]  Stopbits: 1
    [tio 20:29:03]  Parity: none
    [tio 20:29:03]  Local Echo: no
    [tio 20:29:03]  Timestamps: no
    [tio 20:29:03]  Output delay: 0
    ```

5. If it doesn't work, check settings **115200 8N1**. 
    
    And I bet you didn't listen to me when I said that Hardware Flow Control needs to be set to **OFF** [^7] :P 

## References
[^1]: *Raspberry Pi 3, 4 and Zero W Serial Port Usage*, https://www.abelectronics.co.uk/kb/article/1035/raspberry-pi-3--4-and-zero-w-serial-port-usage 
[^2]: *UART configuration*, https://www.raspberrypi.org/documentation/configuration/uart.md
[^3]: *RPi Serial Connection*, https://elinux.org/RPi_Serial_Connection
[^4]: *Linux tells me a serial port is in use, but it isn't*, https://superuser.com/questions/794309/linux-tells-me-a-serial-port-is-in-use-but-it-isnt
[^5]: *5 Linux / Unix Commands For Connecting To The Serial Console*, https://www.cyberciti.biz/hardware/5-linux-unix-commands-for-connecting-to-the-serial-console/ 
[^6]: *Serial communication on modern Linux*, https://opensource.com/article/20/5/tio-linux 
[^7]: *Serial console connection problems*, https://forums.gentoo.org/viewtopic-t-731786-start-0.html
