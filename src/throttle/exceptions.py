#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.core.exceptions import PermissionDenied, ImproperlyConfigured

class RateLimitExceeded(PermissionDenied):
    pass

class ThrottleCoolDownNotDefined(ImproperlyConfigured):
    pass

#class ThrottlePreventFunctionNotDefined(ImproperlyConfigured):
#    pass

#class ThrottleImproperlyConfigure(ImproperlyConfigured):
#    pass
