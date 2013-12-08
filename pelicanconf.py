#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals, print_function

import os

AUTHOR = u'seafile team'
SITENAME = u"Seafile BLOG"
SITEURL = ''

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

PLUGIN_PATH = 'plugins'
PLUGINS = []

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

SOCIAL = (
    ('twitter', 'https://twitter.com/Seafile'),
    ('google groups', 'https://groups.google.com/forum/#!forum/seafile')
)

DEFAULT_PAGINATION = 5

THEMEDIR = 'themes'
THEME = os.path.join(THEMEDIR, 'pelican-bootstrap3')

STATIC_PATHS = [
    'extra/CNAME',
]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}


MARKUP = ('md', 'html')

DISPLAY_CATEGORIES_ON_MENU = False

# Github account info
GITHUB_USER = 'haiwen'
GITHUB_SHOW_USER_LINK = 'true'
GITHUB_SKIP_FORK = True

# DISQUS
DISQUS_SITENAME = 'seafileblog'