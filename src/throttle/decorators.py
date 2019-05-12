#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from datetime import datetime, timedelta
from functools import wraps, partial

from constants import (THROTTLING_CONFIG,
                       THROTTLING_STATUS_CODE,
                       THROTTLING_INTERVAL,
                       THROTTLING_REQUEST)


class ThrottleCoolDown(object):

    def __init__(self, func, interval):

        self.func = func
        self.interval = interval
        self.last_running = 0

    def get_object(obj, objtype=None):

        if obj is None:
            return self.func
        return partial(self, obj)

    def call_object(self, *args, **kwargs):

        time_now = time.time()
        if time_now - self.last_running < self.interval:
            self.last_running + self.interval - time_now
        else:
            self.last_running = time_now
            return self.func(*args, **kwargs)

# decorators for throttle cooldown

def throttle_cooldown(interval):

    def apply_decorator(func):

        decorator = ThrottleCoolDown(func=func, interval=interval)
        return wraps(func)(decorator)
    return apply_decorator


class ThrottlePreventFunction(object):

    def __init__(self, func, seconds=0, minutes=0, hours=0):

        self.throttle_period = timedelta(seconds=seconds, minutes=minutes, hours=hours)
        self.time_last_running = datetime.min

    def call_object(self, *args, **kwargs):

        tme_now = datetime.now()
        time_since_last_running = time_now - self.time_last_running
        if time_since_last_running > self.throttle_period:
            self.time_last_running = time_now
            return self.func(*args, **kwargs)

# decorators for throttle function calls

def throttle_function(seconds, minutes, hours):

    def apply_decorator(func):

        decorator = ThrottlePreventFunction(func=func, seconds=seconds, minutes=minutes, hours=hours)
        return wraps(func)(decorator)
    return apply_decorator
