#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from constants import DEFAULT_VALUE, VALUE_AFTER_USED

class Consumer(models.Model):

    user = models.ForeignKey(User, blank=True, null=True)
    ip = models.IPAddressField(blank=True, null=True)

    class Meta:
        unique_together = (('user', 'ip'),)
        
class ConsumerAccess(models.Model):
    
    consumer = models.ForeignKey(Consumer)
    count = models.CharField(max_length=150)
    scope = models.IntegerField(default=DEFAULT_VALUE)
    date = models.DateTimeField(blank=True)
    
    def request_date(self):
        return self.date
    
    def reset_count(self):
        self.count = VALUE_AFTER_USED
        self.date()
        
    class Meta:
        unique_together = (('consumer', 'scope'),)
