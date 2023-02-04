Title: Termux Dev Setups
Date: 2022-10-27 18:10
Author: @hreikin
Lang: en
Status: hidden
URL: projects/termux-dev-setups
save_as: projects/termux-dev-setups.html

This project includes an easy-to-use script for the installation of a simple developer setup in `Termux` on Android. There are multiple install types to choose from ranging from minimal to a full desktop. [Termux](https://termux.dev/) is a Linux environment and terminal emulator available from [GitHub](https://github.com/termux/termux-app/) and [F-Droid](https://f-droid.org/en/packages/com.termux/).

> Termux is an Android terminal emulator and Linux environment app that works directly with no rooting or setup required. A minimal base system is installed automatically - additional packages are available using the APT package manager.
>
> &nbsp;&nbsp;&nbsp;&nbsp; **<cite>&ndash; Termux Website</cite>**

I created the install script to simplify the process of installing `code-server` or an XFCE desktop environment with `code-oss` installed without having to use a `chroot` or `proot` on a few of the devices I use. A few basic install types are available, such as:

- Minimal - A minimal installation with `code-server` and the `Micro` code editor installed.
- Desktop (VNC) - An XFCE desktop environment accessible via `VNC` with everything from the Minimal install plus `code-oss`, `leafpad` and `firefox` installed.
- Desktop (Xserver) - An XFCE desktop environment accessible via `Xserver` with everything from the Minimal install plus `code-oss`, `leafpad` and `firefox` installed.

## Project Links

For more information about the Termux Dev Setups project check out these links.

- [Termux Dev Setups Github](https://github.com/hreikin/termux-dev-setups)
- [Termux Website](https://termux.dev/)
- [Code Server](https://github.com/coder/code-server)
- [Code OSS](https://github.com/Microsoft/vscode)