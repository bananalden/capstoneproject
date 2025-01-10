from django import forms
from users import models
from django.contrib.auth.hashers import make_password

class add_admin(forms.ModelForm):

    class Meta:
        model = models.CustomUser
        fields = ['first_name','last_name','email','username','password']
        widgets = {
            'password':forms.PasswordInput
        }

        def save(self, commit=True):
            admin = super(add_admin, self).save(commit=False)
            admin.set_password(self.cleaned_data["password"])
            if commit:
                admin.save()
            return admin
