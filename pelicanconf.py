#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'mugwort_rc'
SITENAME = 'Debate Information Laboratory'
SITEURL = ''

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  None

# Social widget
SOCIAL = (('GitHub', 'https://github.com/debate-info-lab'),)

STATIC_PATHS = [
    'img',
    'static',
]

EXTRA_PATH_METADATA = {
    'static/favicon.ico': {
        'path': 'favicon.ico',
    },
}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SLUGIFY_SOURCE = 'basename'
THEME = './pelican-bootstrap3'

