AUTHOR = '@hreikin'
SITENAME = 'hreikin'
TAGLINE = "python developer"
SITEURL = 'https://hreikin.github.io'
THEME = 'pelican-svbhack'
PATH = 'content'
USER_LOGO_URL = SITEURL + '/images/qr-code.png'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_CATEGORY = 'misc'
IGNORE_FILES = ['content/pages/projects/template.md']
STATIC_PATHS = ['images', 'extra/CNAME', 'extra/favicon.ico', 'extra/resume.pdf']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, 'extra/favicon.ico': {'path': 'favicon.ico'}, 'extra/resume.pdf': {'path': 'resume.pdf'},}

# Pelican Search
PELICAN_SEARCH = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
            'linenums': False,
            'guess_lang': False,
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        
        'markdown_link_attr_modifier': {
            'new_tab': 'external_only',
            'no_referrer': 'external_only',
            'auto_title': 'on',
        },
    },
    'output_format': 'html5',
}

# Image Process Plugin
IMAGE_PROCESS = {
    "thumb": {
        "type": "image",
        "ops": ["crop 0 0 50% 50%", "scale_out 150 150 True", "crop 0 0 150 150"],
    },
    "article-image": {
        "type": "image",
        "ops": ["scale_in 600 600 True"],
    },
    "crisp": {
        "type": "responsive-image",
        "srcset": [
            ("1x", ["scale_in 800 600 True"]),
            ("2x", ["scale_in 1600 1200 True"]),
            ("4x", ["scale_in 3200 2400 True"]),
        ],
        "default": "1x",
    },
    "large-photo": {
        "type": "responsive-image",
        "sizes": (
            "(min-width: 1200px) 800px, "
            "(min-width: 992px) 650px, "
            "(min-width: 768px) 718px, "
            "100vw"
        ),
        "srcset": [
            ("600w", ["scale_in 600 450 True"]),
            ("800w", ["scale_in 800 600 True"]),
            ("1600w", ["scale_in 1600 1200 True"]),
        ],
        "default": "800w",
    },
}

# Blogroll
# LINKS = (('Archives', '/archives'),
#          ('Categories', '/categories'),
#          ('Tags', '/tags'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/hreikin'),
          ('Gitlab', 'https://gitlab.com/hreikin'),
          ('Email','mailto:hreikin@gmail.com'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True