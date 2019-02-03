#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Python Portugal Team'
SITENAME = u'Python Portugal'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Lisbon'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URL's
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

ARTICLE_URL = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

YEAR_ARCHIVE_SAVE_AS = 'arquivo/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'arquivo/{date:%Y}/{date:%m}/index.html'
DAY_ARCHIVE_SAVE_AS = 'arquivo/{date:%Y}/{date:%m}/{date:%d}/index.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}.html'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

LOAD_CONTENT_CACHE = False

THEME = 'theme/python-pt'

# Navbar Links da Home Page
NAVBAR_HOME_LINKS = [
    {
        'title': 'Inicio',
        'href': 'inicio',
        'desc': 'Inicio...',
    },
    {
        'title': 'Forum',
        'href': 'forum',
        'desc': 'Forum...',
    },
    {
        'title': 'Inicie-se',
        'href': '#',
        'desc': 'Veja como é fácil começar a usar a linguagem.',
    },
    {
        'title': 'Eventos',
        'href': 'eventos',
        'desc': 'Eventos...',
    },
    {
        'title': 'Aprender',
        'href': '#',
        'desc': (
            'Aprenda ...'
        ),
        'children': [
            {
                'title': 'Tutoriais',
                'href': 'tutoriais',
            },
            {
                'title': 'Livros',
                'href': 'livros',
            },
            {
                'title': 'videos',
                'href': 'videos',
            },
            {
                'title': 'Documentação',
                'href': 'https://docs.python.org',
            },
        ]
    },
    {
        'title': 'Participe',
        'href': '#',
        'desc': (
            'Participe...'
        ),
        'children': [
            {
                'title': 'Mailling List',
                'href': 'https://groups.google.com/forum/#!forum/python-pt',
            },
            {
                'title': 'Facebook',
                'href': 'https://www.facebook.com/python.pt',
            },
            {
                'title': 'Twitter',
                'href': 'https://twitter.com/pythonpt',
            },
        ]
    },
]
