# [hreikin.co.uk](https://hreikin.co.uk)

This repository holds the files for my website [hreikin.co.uk](https://hreikin.co.uk).

## Instructions

### Setup

```sh
git clone --recurse-submodules https://github.com/hreikin/hreikin.github.io.git     # Clone repository
cd hreikin.github.io                                                                # Change in to the new repository
python -m venv .venv                                                                # Create venv
source .venv/bin/activate                                                           # Source venv
pip install -r requirements.txt                                                     # Install development requirements
```

### Usage

During development:

```python
pelican content                     # Build the site
pelican --listen --ignore-cache     # Serve on development server at http://127.0.0.1:8000
```

Push changes to build the updated site:

```python
rm -rf output               # Remove old output folder
pelican content             # Generate content in new output folder
ghp-import -n output        # Use ghp-import to update the gh-pages branch
git push origin gh-pages    # Push changes
```