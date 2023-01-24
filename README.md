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

```python
pelican content
pelican --listen --ignore-cache
ghp-import -n output
git checkout gh-pages
git push origin gh-pages
```