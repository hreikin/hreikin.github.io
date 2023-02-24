Title: First Impressions With Software Development On Termux
Date: 2023-02-24 19:56
Category: mobile-dev
Tags: dev, mobile, termux,
Keywords: dev, development, linux, mobile, termux,
Author: @hreikin
Summary: A detailed post on my first impressions with software development using Termux on Android.
Lang: en
Series: Developing Software On Android Using Termux

*I have been using Termux for almost a month now and figured now would be a good time to give an overview of my experiences. This will be the 2nd post in my series on "Developing Software On Android Using Termux", I will cover my general usage and workflow as well as any errors or common pitfalls I have encountered along the way.*

There are multiple workflows I use when developing on my tablet which I will try to outline below. Each has its use case with Dex being my favourite and probably the best all-rounder, however, the other workflows are certainly great alternatives if your tablet doesn't provide a desktop experience.

## Android Workflow

This is the most basic workflow and works surprisingly well, I was apprehensive at first as to how useful it would be but I use this workflow quite often. I use the S-Pen and a Bluetooth keyboard most of the time in this configuration but it also works well using the touch-screen keyboard and tapping with your finger for navigation.

In "Android Mode" the tablet can be used in either the portrait or landscape orientation, I prefer using the tablet in the portrait orientation most of the time in this mode so each app I have open is wider than it would be in split-screen with the landscape orientation. Most Android tablets come with the ability to have 2 or more apps open at the same time via split-screen or pop-up mode which is where this mode shines, this is great when learning a new framework or if you are tracking down a bug and you are constantly referring to the documentation or Stack Overflow and Google.

A mouse works well in this mode but using touch for navigation is my preferred option due to how the UI is geared towards it. Certain actions like trying to click and drag something can be problematic with the mouse depending on which app is being used and it just generally feels a little more clunky to use this way. The touch-screen keyboard works as well as you would expect it to and if you don't have an external keyboard with you is perfectly capable, however, like most people (I assume) I prefer typing on a regular keyboard if typing anything of length.

## Dex Workflow

I use this workflow the most and although Dex is only provided by Samsung most other manufacturers do offer something similar under a different name. This workflow tries to give you a desktop experience on your tablet, it works best when combined with a mouse and keyboard but can also be used via touch and the touch-screen keyboard. The touch-screen keyboard in this mode can be moved, pinned and resized and although I haven't used it much I can see the benefits it provides.

You can open multiple windows and place or resize them as you need with open windows being displayed on a taskbar along the bottom edge of the screen, this doesn't seem like much but when compared to using the application switcher in "Android Mode" I think it helps speed things up and feels more natural.

Another awesome feature that comes with Dex is the ability to connect an external display. This can be done via casting or with a cable with my preference being to use a cable if possible. When casting to an external display the tablet screen is replicated on the external display, I find this mode useable in a pinch but it can be laggy if the network is congested so most of the time I use an HDMI cable if possible. When using an HDMI cable the tablet will display the Android UI and the external display will use Dex. This is brilliant and helps improve the multitasking capabilities available to you with apps allowed to be opened on either screen and both UI types being available to you.

The portrait orientation cannot be used when using Dex on the tablet but if using an external display via an HDMI cable the tablet can still use the portrait orientation while showing the Android UI. I don't tend to use it this way too often but it's nice to have the option as some apps look better this way.

## Termux X11, Chroot & Proot Workflows

The Android and Dex workflows above all happen within the Android UI without the need for a VNC or Xserver client and even though they are great sometimes you might need to use a Linux desktop instead. For example, if you are creating a desktop application that has a GUI then you will probably need to see how it looks while developing it, this isn't possible in Android without using Termux X11, `chroot` or `proot` in combination with either a VNC or Xserver app on Android. If your tablet doesn't come with Dex or something similar then one of these options is the closest you will get to a real desktop experience.

Termux X11 allows you to install a Linux desktop that is accessed via a VNC or Xserver client along with a huge selection of your typical Linux desktop programs and others such as `code-oss`, the open-source version of `vscode`. Termux runs a Linux environment within Android which is a slightly different way of doing things than using a `chroot` or `proot`.

To be able to use a `chroot` your tablet needs to be rooted, however, to use a `proot` it does not. Both methods achieve the same thing and allow you to run an ARM-based Linux OS within Android, with the differences being in their implementation due to the different required permissions on the host machine. This could be useful if Termux doesn't currently have the packages you require and could even be some people's favoured option due to the number of packages available and their familiarity with the OS. Once again, either of these methods requires using a VNC or Xserver client to be able to access them.

## Favourite Setup

So far, I would say my preferred setup is Dex running on the tablet with a Bluetooth mouse and keyboard, it allows you to set up anywhere with minimal things to carry and no weight compared to a laptop. It also features no wires unless charging the tablet in this convenient configuration.

I haven't spoken about the battery life yet as I would like to use it more before I comment on it but I will say so far it has been brilliant. I regularly get a full day's worth of use out of it between charges but most of what I have done hasn't been particularly resource-heavy.

## Conclusion

One of the biggest surprises to me so far has been how much I have used the Android UI, I initially thought it would be too clunky but the experience is far from it. Combined with apps like `termux`, `code-server` and the `kiwi-browser` it is a versatile device that really shines for things like web development. Dex is the cherry on top and provides a brilliant desktop experience with or without using things like a `chroot` or `proot` which for some can add another layer of complexity when just starting to learn.
