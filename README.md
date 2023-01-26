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
pelican content                     # Build the site
pelican --listen --ignore-cache     # Serve on development server at http://127.0.0.1:8000
```

Push changes to build the updated site:

```python
pelican content             # Important step, do not forget!
ghp-import -n output        # Use ghp-import to update the gh-pages branch
git checkout gh-pages       # Checkout gh-pages branch
git push origin gh-pages    # Push changes
```