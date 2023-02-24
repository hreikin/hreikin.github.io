Title: Installation Errors And Solutions
Date: 2023-02-28 15:37
Category: mobile-dev
Tags: dev, mobile, termux,
Keywords: dev, development, linux, mobile, termux,
Author: @hreikin
Summary: A post listing some of the issues I have encountered while developing with Termux.
Lang: en
Series: Developing Software On Android Using Termux
Status: draft

*This will be the 3rd post in my series on "Developing Software On Android Using Termux", I will cover any errors or common pitfalls I have encountered along the way as well as the solutions I used to fix them.*

Most things I have tried so far when developing on my tablet with Termux have worked without any issues but there have been a few stumbling blocks along the way. None of these issues has been major and they tend to be more to do with the installation of a dependency than any other part of development.

### Django & Wagtail

First up was an issue I encountered when using Django and Wagtail, shortly after running the development server the admin site and server would become unresponsive, this was caused by it not finding the required time-zone information. To fix this I simply ran `pip install tzdata` to install it within the virtual environment.

### Streamlit

The next issue I encountered came when I wanted to try out `streamlit` and required multiple fixes for different problems. This sounds quite bad but the solutions were easy enough to find via Google and aren't complicated. The first error required me to `pkg install libarrow-cpp` to fix an issue with `pyarrow` not finding the required `.so` files.

The second issue was because `streamlit` requires `numpy` and `numpy` on Termux needs the `$MATHLIB` variable set before installing otherwise it will fail to build. This is an easy fix albeit with a bit of a quirk which I will get to shortly. Setting the `$MATHLIB` variable is done by running `export MATHLIB="m"` which can be added to your `.bashrc` file if you want it to be permanent. After this, I installed `numpy` before installing `streamlit` which turned out to be a mistake, the installation worked perfectly with the only problem being; even though I had already installed `numpy` when I then installed `streamlit` it proceeded to build and install `numpy` again. I never managed to find out why this happened and as things were now installed I decided to carry on testing instead of figuring it out.

The final error related to `streamlit` came when trying to run the demo but luckily while researching the `numpy` issue I had already found the answer and knew it was the fix straight away. To finally enjoy learning about and testing `streamlit` all I had to do was run `export LDFLAGS="-lpython3.11"` due to a version mismatch.

### Pywebview


