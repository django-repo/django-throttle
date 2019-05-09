#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.conf import settings

DEFAULT_VALUE = 0
VALUE_AFTER_USED = 1

THROTTLING_CONFIG = getattr(settings, 'CONFIG', {})
THROTTLING_STATUS_CODE = getattr(settings, 'STATUS_CODE', 429)
THROTTLING_INTERVAL = getattr(settings, 'INTERVAL', 60*24)
THROTTLING_REQUEST = getattr(settings, 'NUMBER_OF_REQUEST', 1000)
