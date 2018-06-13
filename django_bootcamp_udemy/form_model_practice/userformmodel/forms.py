from .models import User
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }

        fields = ['first_name', 'last_name', 'email', 'password']