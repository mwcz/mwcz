#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

DEBUG = False
SITEURL = 'https://palebluepixel.org'
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

# only use the thumbnailer plugin for production builds because it's sloooooooow
# PLUGINS.append('thumbnailer')
PLUGINS.append('optimize_images')

# Feed (syndication) settings (enabled for production only)
FEED_ATOM             = 'feeds/atom.xml'
FEED_ALL_ATOM         = 'feeds/all.atom.xml'
FEED_RSS              = 'feeds/all.rss.xml'
FEED_ALL_RSS          = 'feeds/rss.xml'
CATEGORY_FEED_ATOM    = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
PIWIK_ANALYTICS = False # until piwik is back up
