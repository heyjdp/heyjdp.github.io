from datetime import datetime

AUTHOR = "Jas Powell"
# SITEURL = "http://localhost:8000"
SITENAME = "heyjdp"
SITETITLE = "Jas Powell"
SITESUBTITLE = "Just some notes"
SITEDESCRIPTION = "Notes about Tech and being a Remote Startup CTO"
SITELOGO = "/images/jas-powell-profile.png"

BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "colorful"
# MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra']

SYNTAX_THEME=u'github'

ROBOTS = "index, follow"

THEME="../pelican-themes/Flex"

PATH = "content"
PATH_PAGES = "pages"
RELATIVE_URLS = True
STATIC_PATHS = ["images", "extra", ]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

TIMEZONE = 'Asia/Nicosia'

I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"
DATE_FORMATS = {
    "en": "%B %d, %Y",
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

GITHUB_CORNER_URL = "https://github.com/heyjdp"

DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = 'docs/'

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

DISPLAY_PAGES_ON_MENU = True

# Blogroll
LINKS = (
    ("Jas Powell", "/author/jas-powell"),
    ("github", "https://www.github.com/heyjdp"),
)

# Social widget
SOCIAL = (
    ("github", "https://github.com/heyjdp"),
    ("rss", "/feeds/all.atom.xml"),
)

VERSION = u'1.0.0'
COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True
