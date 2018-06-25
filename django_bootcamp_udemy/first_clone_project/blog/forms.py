from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile, Post


class ProfileCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Profile
        fields = ('username', 'email')


class ProfileChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = Profile
        fields = UserChangeForm.Meta.fields


class PostCreationForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'profile',)
        widgets = {'text': forms.Textarea()}
