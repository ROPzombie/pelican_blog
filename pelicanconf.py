#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '0x00'
SITENAME = '0x00s blog'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['pdfs', 'images']

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'de'

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins', 'pelican-plugins']
PLUGINS = ['ipynb.markup', 'render_math', 'jinja2content', 'tag_cloud', 'i18n_subsites']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

THEME = 'pelican-bootstrap3'

#JINJA_EXTENSIONS = ['jinja2.ext.i18n']


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Content licensing: CC-BY
CC_LICENSE = "CC-BY"

# LINKS
#LINKS = (('Project Euler', 'https://projecteuler.net/'), ('Hackerrank', 'https://www.hackerrank.com/'),)

# Social widget
SOCIAL = (('@github', 'https://github.com/sh3llc0d3r'),
            ('@twitter', 'https://twitter.com/0xdeadbeef6'),
          ('z01db3rg@gitlab.com', 'https://gitlab.com/z01db3rg'))

DEFAULT_PAGINATION = 10

IGNORE_FILES = ['.ipynb_checkpoints']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

