from __future__ import unicode_literals

AUTHOR = 'The VIANNA research team'
SITENAME = 'VIANNA'
SITEURL = ''

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'  # use filesystem date if not given in article
USE_FOLDER_AS_CATEGORY = True

THEME = './themes/VIANNA-theme'
BOOTSTRAP_THEME = 'yeti'  # from http://bootswatch.com/yeti

# Some hand-crafted entries (links) in the main menu
# MENUITEMS = [('foo', 'http://foo.org')]

# Links to external partners
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social stuff?
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)


###############################################################################
# Technical stuff ahead. You probably don't need to worry beyond this point.
###############################################################################

OUTPUT_PATH = "html"

DISPLAY_CATEGORIES_ON_MENU = True

DEFAULT_CATEGORY = "news"

# Always copy these to output, so they get uploaded.
STATIC_PATHS = ['__downloads']

# The name of the dir containing the static pages to put into the menu
# PAGE_PATHS = ['__pages']

# The dir to process input files
PATH = 'homepage'

DEFAULT_PAGINATION = True

# We don't need a page listing the different authors
AUTHORS_SAVE_AS = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True  # Note: gets overwritten in production setup!

# The plugins to load
# Note, `hierarchy` is our own plugin for hierachic static pages.
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['hierarchy']
# PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
#            'liquid_tags.youtube', 'liquid_tags.include_code',
#            'liquid_tags.notebook',
#            'hierarchy']

# Needed for inclusion of IPython notebooks
# See <https://github.com/getpelican/pelican-plugins/tree/master/liquid_tags>
# if os.path.exists('_nb_header.html'):
#     EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# STATIC_LANG_SAVE_AS = "{path}-{lang}"

# Extract title, slug and optionally the language from filename
# (Note: The file extension and the dot have already been stripped).
# The extraction of title, slug and lang from the file name avoids the most
# common "title not defined" error and makes defining :title and :slug
# and :lang in a page optional.
# Example file name: `Here-is-my-post-en.md`
# Will set both, title and slug to "Here-is-my-post" and the lang to "en"
# The `((?!-(en|de)).)+` part matches one or more (`+`) of any char (`.`) but
# not if the next chars are `-en` or `-de`.
# Use http://www.pyregex.com to test this Regex.
# FILENAME_METADATA = r'(?P<order>[0-9]*(_|-| ))?(?P<slug>(?P<title>((?!-(en|de)).)+))(-(?P<lang>(en|de)))?'
FILENAME_METADATA = r'(?P<order>[0-9]*(_|-| ))?(?P<slug>(?P<title>((?!-(en|de)).)+))(-(en|de))?'
