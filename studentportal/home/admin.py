from django.contrib import admin
from .models import User
from .forms import NewUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class NewAdmin(UserAdmin):
    model = User
    add_form = NewUserCreationForm

admin.site.register(User)