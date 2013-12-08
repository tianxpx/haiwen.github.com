#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals, print_function

import os

AUTHOR = u'seafile team'
SITENAME = u"Seafile BLOG"
SITEURL = ''

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/Seafile'),
    ('google groups', 'https://groups.google.com/forum/#!forum/seafile')
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEMEDIR = 'themes'
THEME = os.path.join(THEMEDIR, 'pelican-bootstrap3')

MARKUP = ('rst', 'md', 'html')

PLUGIN_PATH = 'plugins'
PLUGINS = []

DISPLAY_CATEGORIES_ON_MENU = False

GITHUB_USER = 'haiwen'
GITHUB_SHOW_USER_LINK = 'true'
GITHUB_SKIP_FORK = True