from django.shortcuts import redirect
from django.urls import reverse

class ForcePasswordChangeMiddleware:
    """
    Middleware to force users who are inactive (is_active=False)
    to change their password on first login.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user

        # Exclude unauthenticated users, admin, and already active users
        if user.is_authenticated and not user.is_active:
            allowed_paths = [
                reverse('authentication:first-login-password'),
                reverse('authentication:logout'),
            ]
            if request.path not in allowed_paths:
                return redirect('authentication:first-login-password')

        return self.get_response(request)
