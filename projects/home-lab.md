---
layout: landing
title: Home Lab
description: A Place For Me To Learn And Play
image: assets/images/home-lab-04.png
nav-menu: false
show_tile: false
---

<!-- Main -->
<div id="main">

<!-- One -->
<section id="one">
	<div class="inner">
		<header class="major">
			<h2>What Is A Home Lab ?</h2>
		</header>
		<p>There isn't really a set definition for the term 'Home Lab' as it means different things to different people, I'd personally describe it as something that someone could use to learn, test or tinker. I use my Home Lab for studying along with hosting various different services at home. The practical experience it brings me is invaluable in my journey to becoming a System Admin as it allows me to practice the things I have learned in the safety of my own environment. I am only just beginning my studying so it is currently cobbled together from various pieces of old hardware I have laying around but for me it is perfect. The <a href="https://www.techrepublic.com/">Tech Republic</a> describes a Home Lab as follows.</p>
        <blockquote cite="https://www.techrepublic.com/article/tech-projects-for-it-leaders-how-to-build-a-home-lab/">
            <p>Think of a home lab as the technology equivalent of the scientist's laboratory. It's a place where you can experiment with new technologies, attempt to interconnect various services in novel ways and quickly clean things up when you're done. While you might be picturing a huge rack of howling servers, fortunately for us you can now create the equivalent of a small data center on a single piece of physical equipment.</p>
            <figcaption><b>— <cite>Tech Republic Website</cite></b></figcaption>
        </blockquote>
        <p>My current Home Lab is very basic and quite small compared to most others I have seen online in places like <a href="https://www.reddit.com/r/homelab/" target="_blank">r/homelab</a> but it works perfectly for what I need it to and apart from the ethernet switch it is made up entirely of hardware that was sitting around doing nothing. On top of the listed items below I also have my desktop and laptop which I use for day to day tasks as well as managing the services I have running over the network via SSH or the browser.</p>
		<ul>
            <li>5 Port TP-Link Managed Ethernet Switch</li>
            <li>2 x Raspberry Pi 1 Model B</li>
            <li>1 x Raspberry Pi Zero 2</li>
            <li>1 x Odroid U3</li>
            <li>1 x Intel Atom Netbook</li>
            <li>1 x 320 GB USB Hard Drive</li>
            <li>1 x TFT LCD Touch Screen</li>
		</ul>
        <header class="major">
			<h2>What Services Do I Host ?</h2>
		</header>
        <p>I have quite a few different services running on my various devices and will try and outline them all now with a little description about what each one does. The 2 Raspberry Pi Model B's are running DietPi as their OS which is a Debian derivitive optimized to work on SBC's. One of them I have running PiHole and PiVPN for network-wide adblocking and access to my network from anywhere via the PiVPN server while the other hosts ownCloud for the family to keep their photos backed up. The Odroid U3 is running Arch and is my Docker machine which runs the following containers which are mainly for monitoring my network and providing detailed stats about each machine; Homer Dashboard, FreshRSS, Prometheus, Grafana, Uptime Kuma, Gotify and Portainer. The netbook I use to host my BookStack wiki while the Raspberry Pi Zero 2 has an Apache web server running and is also my Docker test machine that I use for trying out various programs and services to see if I like them before deploying them to the Odroid U3.</p>
        <section class="row">
            <a class="image column" href="../assets/images/home-lab-01.png" target="_blank">
                {% responsive_image path: assets/images/home-lab-01.png alt: "Simple Side Scroller Level Editor Preview" title: "Simple Side Scroller Level Editor Preview" %}
            </a>
            <a class="image column" href="../assets/images/home-lab-02.png" target="_blank">
                {% responsive_image path: assets/images/home-lab-02.png alt: "Simple Side Scroller Blueprint" title: "Simple Side Scroller Blueprint" %}
            </a>
        </section>
        <section class="row">
            <a class="image column" href="../assets/images/home-lab-03.png" target="_blank">
                {% responsive_image path: assets/images/home-lab-03.png alt: "Simple Side Scroller Player" title: "Simple Side Scroller Player" %}
            </a>
            <a class="image column" href="../assets/images/home-lab-04.png" target="_blank">
                {% responsive_image path: assets/images/home-lab-04.png alt: "Simple Side Scroller Boss Level Editor Preview" title: "Simple Side Scroller Boss Level Editor Preview" %}
            </a>
        </section>
        <section class="row">
            <a class="image column" href="../assets/images/home-lab-05.png" target="_blank">
                {% responsive_image path: assets/images/home-lab-05.png alt: "Simple Side Scroller Player" title: "Simple Side Scroller Player" %}
            </a>
            <a class="image column" href="../assets/images/home-lab-06.png" target="_blank">
                {% responsive_image path: assets/images/home-lab-06.png alt: "Simple Side Scroller Boss Level Editor Preview" title: "Simple Side Scroller Boss Level Editor Preview" %}
            </a>
        </section>
        <p style="padding-top: 1.5em;">Each of these little machines runs perfectly for what I have been using them for and still has room to grow without taking up much space or costing much in electricity either. Next on my wishlist is a Raspberry Pi 4B with a Cluster HAT and 4 x Raspberry Pi Zero 2's so I can practice cluster computing at home with an affordable setup.</p>
	</div>
</section>

<!-- Two -->
<section id="two">
	<div class="inner">
		<header class="major">
			<h2>Project Links</h2>
		</header>
		<p>For more information about Home Labs and Self Hosting check out these links.</p>
		<ul>
            <li><a href="https://www.reddit.com/r/homelab/" target="_blank">r/Homelab</a></li>
            <li><a href="https://www.reddit.com/r/homelab/wiki/index" target="_blank">r/Homelab Wiki</a></li>
            <li><a href="https://www.reddit.com/r/selfhosted/" target="_blank">r/Selfhosted</a></li>
            <li><a href="https://www.reddit.com/r/selfhosted/wiki/index" target="_blank">r/Selfhosted Wiki</a></li>
		</ul>
	</div>
</section>

<!-- Main End -->
</div>
