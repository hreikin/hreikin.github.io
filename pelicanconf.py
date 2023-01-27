AUTHOR = '@hreikin'
SITENAME = 'hreikin'
TAGLINE = "developer"
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
STATIC_PATHS = ['extra/favicon.ico']
EXTRA_PATH_METADATA = {'extra/favicon.ico': {'path': 'favicon.ico'},}

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