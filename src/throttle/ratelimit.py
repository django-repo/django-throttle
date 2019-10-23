from collections import Counter
from rest_framework.throttling import SimpleRateThrottle
from django.contrib.auth.models import User


class PreventUserThrottle(SimpleRateThrottle):

    """
	class for implement throttling and block
	anon user or registered user. It will be
	blocking particular user that given by his/her
	name and block their IP address after 3-6 login
	attempts
	"""

    scope = "UserAttempts"

    def get_cache(self, request, view):

        user = User.objects.filter(username=request.data.get("username"))
        ident = user[0].pk if user else self.get_ident(request)

        return self.cache_format % {"scope": self.scope, "ident": ident}

    def throttle_success(self, request):

        user = User.objects.filter(username=request.data.get("username"))
        if user:
            self.history.insert(0, user[0].id)
        self.history.insert(0, self.now)
        self.cache.set(self.key, self.history, self.duration)
        return True

    def allow_request(self, request, view):

        if self.rate is None:
            return True

        self.key = self.get_cache(request, view)
        if self.key is None:
            return True

        self.history = self.cache.get(self.key, [])
        self.now = self.timer()

        while self.history and self.history[-1] <= self.now - self.duration:
            self.history.pop()

        if len(self.history) >= self.num_requests:
            return self.throttle_failure()

        if len(self.history) >= 3:
            data = Counter(self.history)
            for value in data.items():
                if value == 2:
                    return self.throttle_failure()
        return self.throttle_success(request)