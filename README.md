# [hreikin.co.uk](https://hreikin.co.uk)

This repository holds the files for my website [hreikin.co.uk](https://hreikin.co.uk).

## Instructions

### Setup

```sh
git clone --recurse-submodules https://github.com/hreikin/hreikin.github.io.git
cd hreikin.github.io
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Usage

During development:

```python
pelican content
pelican --listen --ignore-cache
```

Push changes to build the updated site (this seems convoluted, research is required on using a submodule for the theme as I think this is what is causing the issues):

```python
git checkout gh-pages
rm -rf pelican-svbhack
git checkout pelican
cd pelican-svbhack
git submodule update
cd ..
ghp-import -n output
git checkout gh-pages
git push origin gh-pages
```