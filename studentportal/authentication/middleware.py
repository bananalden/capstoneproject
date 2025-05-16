from django.shortcuts import redirect
from django.urls import reverse

class ForcePasswordResetMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return self.get_resonse(request)
        
        if request.user.is_active:
            return self.get_response(request)
        
        allowed_paths = {
            reverse('authentication:set-new-pass'),
            reverse('authentication:logout_user')
        }

        if request.path not in allowed_paths:
            return redirect('authentication:set-new-pass')
        
        return self.get_response(request)