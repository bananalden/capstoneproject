from django.contrib.auth.backends import ModelBackend

class AllowInactiveUserBackend(ModelBackend):
    def user_can_authenticate(self, user):
        return True  # Allow even if is_active is False
