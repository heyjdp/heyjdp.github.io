--- 
title: "\U0001f4bb Strip Image EXIF Data \U0001f4f8 \U0001f469\u200D\U0001f4bb \U0001f427"
date: 2021-12-21T09:00:00+02:00 
draft: false 
tags: ["tech", "linux", "commandline", "exif data"] 
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
    image: "/post-img/image-metadata-1200x628.jpg" # image path/url
    alt: "Trinity from Matrix hacking on the Linux commandline" # alt text
#    caption: "" # display caption under cover
    relative: false # when using page bundles set this to true
    hidden: false # only hide on current single page
---

Did you know that all of your images contain a bunch of metadata? This is mostly harmless. But actually some of the [metadata is not harmless](https://www.newyorker.com/news/news-desk/whats-the-matter-with-metadata).

<!-- more -->

Dianne Feinstein, an American, famously said, post-Snowden, that "Our courts have consistently recognized that there is no reasonable expectation of privacy in this type of metadata information and thus no search warrant is required to obtain it". Yikes!

Also, note that the EFF have thoughts on fingerprinting of digital cameras, printers, CD ROM burners, and MAC addresses in routing devices. This article is about their concerns about [electronic tracking via unique identifiers like EXIF serial numbers](https://www.eff.org/deeplinks/2007/07/harry-potter-and-digital-fingerprints).

## EXIF Data

EXIF Data stands for Exchangeable Image File MetaData, which is embedded within the captured photograph captured by any digital camera. EXIF data has the technical information behind a particular click, which helps viewers understand what technical skills and knowledge was used by the photographer to click a picture.

This includes information on camera lens and model, exposure settings, focal length, and regular description of the picture. While such data is a source of both information and knowledge, especially for someone who studies photography, EXIF data can also prove dangerous and threatening to owner privacy. This is because, besides all the technical factors, the EXIF data also include GPS location, owner name, and personal details. Such data is added to retain ownership and copyright over a picture if it ever has to be released on a public platform.

## Stripping EXIF Data

If you have the `gimp` tool installed on lLinux it is a simple as going to the directory containing all the images and:

```bash
cd images
mogrify -strip *.jpg
```

This stackoverflow has great info about mogrify and strip: [mofgrify strip answer](https://askubuntu.com/questions/260810/how-can-i-read-and-remove-meta-exif-data-from-my-photos-using-the-command-line/968598#968598)

## Another option: `exiftool`

The `exiftool` can be used for a similar purpose. First install it:

```bash
sudo apt install libimage-exiftool-perl
```

Now view all the metadata on a file (the `XXXX` were added by me to anonymize somewhat):

```bash
$ exiftool photo_metadata_orig.jpg 
ExifTool Version Number         : 11.16
File Name                       : photo_metadata_orig.jpg
Directory                       : .
File Size                       : 1451 kB
File Modification Date/Time     : 20XX:03:18 XX:29:32+02:00
File Access Date/Time           : 20XX:03:18 XX:29:46+02:00
File Inode Change Date/Time     : 20XX:03:18 XX:32:53+02:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Profile CMM Type                : Apple Computer Inc.
Profile Version                 : 4.0.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 2017:XX:XX XX:22:XX
Profile File Signature          : acsp
Primary Platform                : Apple Computer Inc.
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : Apple Computer Inc.
Device Model                    : 
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Apple Computer Inc.
Profile ID                      : ca1a95822XXXXXXXXXXXXXXXX1ea1582
Profile Description             : Display P3
Profile Copyright               : Copyright Apple Inc., 2017
Media White Point               : 0.95045 1 1.08905
Red Matrix Column               : 0.51512 0.2412 -0.00105
Green Matrix Column             : 0.29198 0.69225 0.04189
Blue Matrix Column              : 0.1571 0.06657 0.78407
Red Tone Reproduction Curve     : (Binary data 32 bytes, use -b option to extract)
Chromatic Adaptation            : 1.04788 0.02292 -0.0502 0.02959 0.99048 -0.01706 -0.00923 0.01508 0.75168
Blue Tone Reproduction Curve    : (Binary data 32 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 32 bytes, use -b option to extract)
Image Width                     : 3024
Image Height                    : 4032
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Image Size                      : 3024x4032
Megapixels                      : 12.2
```

That's a *lot* of data, sure most of it is only for recreating the image in it's best format (the RGB curves and white points), but there is also that sneaky **Profile ID** in there.

I don't work for Apple, so I don't know for sure, but I am pretty sure that is a unique ID for my account and can be traced to me, my credit card purchases, my GPS locations, etc.

So... how do we [strip the EXIF junk](https://linuxnightly.com/how-to-remove-exif-data-via-linux-command-line/)?

```bash
$ exiftool -all= photo_metadata_orig.jpg 
    1 image files updated

$ exiftool photo_metadata_orig.jpg 
ExifTool Version Number         : 11.16
File Name                       : photo_metadata_orig.jpg
Directory                       : .
File Size                       : 1451 kB
File Modification Date/Time     : 20XX:03:18 XX:29:32+02:00
File Access Date/Time           : 20XX:03:18 XX:29:46+02:00
File Inode Change Date/Time     : 20XX:03:18 XX:32:53+02:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
Image Width                     : 3024
Image Height                    : 4032
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Image Size                      : 3024x4032
Megapixels                      : 12.2
```

Et, voila!
