Title: Arch Linux ARM Packages
Date: 2023-01-12 18:10
Author: @hreikin
Lang: en
Status: hidden
URL: projects/arch-linux-arm-packages
save_as: projects/arch-linux-arm-packages.html

I created the PKGBUILD's inside this repository to fix some of the earlier issues with running Arch Linux ARM and other software on the Odroid U3, ALARMDROID is the repository I created to store them in. The Odroid U3 is a Single Board Computer (SBC) much like the Raspberry Pi but with a more powerful CPU and more RAM. The Odroid U3 has been discontinued and is no longer on sale or supported but newer boards are available from HardKernel. More information about the Odroid U3 can be found at the [HardKernel Website](https://www.hardkernel.com/shop/odroid-u3/) and a brief description of it is shown below.

>The ODROID-U3 is a very low cost and high performance development platform based on an Exynos 4412 ARM Cortex-A9 Quad Core 1.7GHz CPU. It has 3 USB 2.0 ports and micro HDMI. The board has several accessories available through Hardkernel such as 10.1" and 14" LVDS LCDs (with adapters), Wifi and Bluetooth adapters, 1.8v serial adapter, and an eMMC storage module.
>
> &nbsp;&nbsp;&nbsp;&nbsp; **<cite>&ndash; Arch Linux ARM</cite>**

The packages in my ALARMDROID repository are based on some original work done by [@gripped](https://github.com/gripped) for the Odroid U2 which was an earlier version of the Odroid U3. The PKGBUILD's build and package programs such as Kodi and FFmpeg for example with changes and optimizations to get them running on the Odroid U3's hardware. These packages are no longer needed as the work upstream has superseded them and they were only created as a work-around to get things going until the upstream work was completed. If you want to find out more information about my Arch Linux ARM Packages or the Odroid U3 then please check out the project links that I have listed down below.

## Project Links

For more information about my Arch Linux ARM packages or the Odroid U3 check out these links.

- [Arch Linux ARM Packages GitHub Repository](https://github.com/hreikin/ALARMDROID)
- [Arch Linux ARM Documentation](https://archlinuxarm.org/platforms/armv7/samsung/odroid-u3)
- [Odroid U3 Product Page](https://www.hardkernel.com/shop/odroid-u3/)
- [HardKernel Official Website](https://www.hardkernel.com/)
- [HardKernel Documentation](https://wiki.odroid.com/)