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
SOCIAL = (
    ('GitHub', 'https://github.com/info-labs'),
    ('Twitter', 'https://twitter.com/InfoLabs_jp'),
)

STATIC_PATHS = [
    'img',
    'static',
]

EXTRA_PATH_METADATA = {
    'static/CNAME': {
        'path': 'CNAME',
    },
    'static/android-icon-36x36.png': {
        'path': 'android-icon-36x36.png',
    },
    'static/android-icon-48x48.png': {
        'path': 'android-icon-48x48.png',
    },
    'static/android-icon-72x72.png': {
        'path': 'android-icon-72x72.png',
    },
    'static/android-icon-96x96.png': {
        'path': 'android-icon-96x96.png',
    },
    'static/android-icon-144x144.png': {
        'path': 'android-icon-144x144.png',
    },
    'static/android-icon-192x192.png': {
        'path': 'android-icon-192x192.png',
    },
    'static/apple-icon.png': {
        'path': 'apple-icon.png',
    },
    'static/apple-icon-57x57.png': {
        'path': 'apple-icon-57x57.png',
    },
    'static/apple-icon-60x60.png': {
        'path': 'apple-icon-60x60.png',
    },
    'static/apple-icon-72x72.png': {
        'path': 'apple-icon-72x72.png',
    },
    'static/apple-icon-76x76.png': {
        'path': 'apple-icon-76x76.png',
    },
    'static/apple-icon-114x114.png': {
        'path': 'apple-icon-114x114.png',
    },
    'static/apple-icon-120x120.png': {
        'path': 'apple-icon-120x120.png',
    },
    'static/apple-icon-144x144.png': {
        'path': 'apple-icon-144x144.png',
    },
    'static/apple-icon-152x152.png': {
        'path': 'apple-icon-192x192.png',
    },
    'static/apple-icon-180x180.png': {
        'path': 'apple-icon-180x180.png',
    },
    'static/apple-icon-precomposed.png': {
        'path': 'apple-icon-precomposed.png',
    },
    'static/browserconfig.xml': {
        'path': 'broserconfig.xml',
    },
    'static/favicon.ico': {
        'path': 'favicon.ico',
    },
    'static/favicon-16x16.png': {
        'path': 'favicon16x16.png',
    },
    'static/favicon32x32.png': {
        'path': 'favicon32x32.png',
    },
    'static/favicon96x96.png': {
        'path': 'favicon96x96.png',
    },
    'static/manifest.json': {
        'path': 'manifest.json',
    },
    'static/ms-icon-70x70.png': {
        'path': 'ms-icon-70x70.png',
    },
    'static/ms-icon-144x144.png': {
        'path': 'ms-icon-144x144.png',
    },
    'static/ms-icon-150x150.png': {
        'path': 'ms-icon-150x150.png',
    },
    'static/ms-icon-310x310.png': {
        'path': 'ms-icon-310x310.png',
    },
}

DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SLUGIFY_SOURCE = 'basename'
THEME = './pelican-bootstrap3'

