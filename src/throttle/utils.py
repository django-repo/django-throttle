#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from models import Consumer

def get_or_create_consumer(request):

    if request.is_authenticated():
        return get_or_create_authenticated_consumer(request)
    return get_or_create_anonymous_consumer(request)

def get_or_create_authenticated_consumer(request):

    consumer, created = Consumer.objects.get_or_create(user=request.user)

def get_or_create_anonymous_consumer(request):

    consumer, created = Consumer.objects.get_or_create(ip=request.META['REMOTE_ADDR'])
