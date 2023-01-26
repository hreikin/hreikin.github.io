Title: Developing On Android
Date: 2023-01-12 10:30
Category: mobile-dev
Tags: dev, mobile, termux,
Keywords: dev, development, linux, mobile, termux,
Author: @hreikin
Summary: An introduction to development on Android using Termux.
Lang: en
Status: draft

Using Android for software or web development hasn't always been an easy or stable experience in the past however in recent years it has come on leaps and bounds. Previously I have used my phone to do things in a pinch when I have had no other option but recently I bought myself a tablet and wanted to see how feasible it would be to use it for software or web development and how far I could push it before running into any deal-breaking issues.

I have never owned my own tablet but the family has so as this was a rare treat for myself I decided to choose a high-end one. The tablet in question is a Samsung S8 Ultra that comes with:

- 256 GB storage (expandable by microSD)
- 12 GB of RAM
- 8-core Snapdragon SM8450
- Adreno 730 GPU
- a 14.6 inch Super AMOLED screen
- an S-Pen

It's the 2nd or 3rd best model they do with one being available with 16 GB of RAM but it was the best that was available that I could find for purchase and I am extremely happy with it. It cannot be considered cheap costing around £1000 but it is a high-end tablet with some great specifications.

## Termux

Termux is a terminal emulator and Linux environment application available on Android. It requires no rooting or setup. A small base system is installed automatically and additional packages are available via `apt` or `pkg`. It is available on [Github](https://github.com/termux/termux-app) or [F-Droid](https://f-droid.org/packages/com.termux/). Do not install the Google Play version as it hasn't been updated in a long time due to some external issues.

Termux allows you to setup a Linux development machine fairly easily, I have made a few Bash scripts (Github repository available [here](https://github.com/hreikin/termux-dev-setups)) to simplify it even further and wont go into detail about the process but once Termux is installed then using one of my scripts I will have access to a variety of programs such as:

- Code Server and/or Code OSS
- Python
- Git
- Firefox
- XFCE desktop envionment

This is extremely useful as I'm sure you can tell, my installation script offers a minimal or desktop version with a few key differences. The minimal version comes with Code Server which allows you to run a locally available, open-source version of VS Code accessible from an Android or desktop browser. The desktop version is accessible via VNC or XserverSDL and comes with Code OSS whch is the open-source version of VS Code.

## Dex Mode