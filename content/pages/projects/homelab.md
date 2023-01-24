Title: What Is A Home Lab ?
Date: 2023-01-12 18:10
Author: @hreikin
Lang: en
Status: hidden
URL: projects/homelab
save_as: projects/homelab.html

There isn't really a set definition for the term 'Home Lab' as it means different things to different people, I'd personally describe it as something that someone could use to learn, test or tinker. I use my Home Lab for studying along with hosting various different services at home. The practical experience it brings me is invaluable in my journey to becoming a System Admin as it allows me to practice the things I have learned in the safety of my own environment. I am only just beginning my studying so it is currently cobbled together from various pieces of old hardware I have laying around but for me it is perfect. The [Tech Republic](https://www.techrepublic.com/) describes a Home Lab as follows.

>Think of a home lab as the technology equivalent of the scientist's laboratory. It's a place where you can experiment with new technologies, attempt to interconnect various services in novel ways and quickly clean things up when you're done. While you might be picturing a huge rack of howling servers, fortunately for us you can now create the equivalent of a small data center on a single piece of physical equipment.
>
> &nbsp;&nbsp;&nbsp;&nbsp; **<cite>&ndash; Tech Republic Website</cite>**

My current Home Lab is very basic and quite small compared to most others I have seen online in places like [r/homelab](https://www.reddit.com/r/homelab/) but it works perfectly for what I need it to and apart from the ethernet switch it is made up entirely of hardware that was sitting around doing nothing. On top of the listed items below I also have my desktop and laptop which I use for day to day tasks as well as managing the services I have running over the network via SSH or the browser.

- 5 Port TP-Link Managed Ethernet Switch
- 2 x Raspberry Pi 1 Model B
- 1 x Raspberry Pi Zero 2
- 1 x Odroid U3
- 1 x Intel Atom Netbook
- 1 x 320 GB USB Hard Drive
- 1 x TFT LCD Touch Screen

## What Services Do I Host ?

I have quite a few different services running on my various devices and will try and outline them all now with a little description about what each one does. The 2 Raspberry Pi Model B's are running DietPi as their OS which is a Debian derivitive optimized to work on SBC's. One of them I have running PiHole and PiVPN for network-wide adblocking and access to my network from anywhere via the PiVPN server while the other hosts ownCloud for the family to keep their photos backed up. The Odroid U3 is running Arch and is my Docker machine which runs the following containers which are mainly for monitoring my network and providing detailed stats about each machine:

- Homer Dashboard
- FreshRSS
- Prometheus
- Grafana
- Uptime Kuma
- Gotify
- Portainer

The netbook I use to host my BookStack wiki while the Raspberry Pi Zero 2 has an Apache web server running and is also my Docker test machine that I use for trying out various programs and services to see if I like them before deploying them to the Odroid U3.

<a href="/images/home-lab-01.png" target="_blank">
    <img src="/images/home-lab-01.png" />
</a>
<a href="/images/home-lab-02.png" target="_blank">
    <img src="/images/home-lab-02.png" />
</a>
<a href="/images/home-lab-03.png" target="_blank">
    <img src="/images/home-lab-03.png" />
</a>
<a href="/images/home-lab-04.png" target="_blank">
    <img src="/images/home-lab-04.png" />
</a>
<a href="/images/home-lab-05.png" target="_blank">
    <img src="/images/home-lab-05.png" />
</a>
<a href="/images/home-lab-06.png" target="_blank">
    <img src="/images/home-lab-06.png" />
</a>

Each of these little machines runs perfectly for what I have been using them for and still has room to grow without taking up much space or costing much in electricity either. Next on my wishlist is a Raspberry Pi 4B with a Cluster HAT and 4 x Raspberry Pi Zero 2's so I can practice cluster computing at home with an affordable setup.

## Project Links

For more information about Home Labs and Self Hosting check out these links.

- [r/Homelab](https://www.reddit.com/r/homelab/)
- [r/Homelab Wiki](https://www.reddit.com/r/homelab/wiki/index)
- [r/Selfhosted](https://www.reddit.com/r/selfhosted/)
- [r/Selfhosted Wiki](https://www.reddit.com/r/selfhosted/wiki/index)
