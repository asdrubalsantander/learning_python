from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import ProfileChangeForm, ProfileCreationForm
from .models import Profile, Post, Comment


class ProfileAdmin(UserAdmin):
    add_form = ProfileCreationForm
    form = ProfileChangeForm
    model = Profile
    list_display = ['email', 'username', 'name']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post)
admin.site.register(Comment)
