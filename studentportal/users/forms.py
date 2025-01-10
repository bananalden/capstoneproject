from django import forms
from django.contrib.auth.forms import UserCreationForm
from users import models

class add_admin(UserCreationForm):

    class Meta:
        model = models.CustomUser
        fields = ['first_name','last_name','email','username','password1']
        widgets = {
            'password':forms.PasswordInput
        }

    def __init__(self, *args, **kwargs):
        super(add_admin, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None
