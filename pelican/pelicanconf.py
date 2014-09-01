#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Richard Gray'
SITENAME = u'crash.net.nz'
SITEURL = 'http://crash.net.nz'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

DATE_FORMATS = {
    'en': '%b %d, %Y',
}

TYPOGRIFY = True

OUTPUT_PATH = 'output/'
PATH = 'content/'
THEME = 'themes/crash'
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'blog'

# Caching
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'))

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/elvortura'),
          ('Github', 'https://github.com/vortura'),
          ('Last.fm', 'http://www.last.fm/user/vortura'),
          ('Flickr', 'https://secure.flickr.com/photos/richardgray/'),)

DEFAULT_PAGINATION = False

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

GOOGLE_ANALYTICS = 'UA-19608372-1'
