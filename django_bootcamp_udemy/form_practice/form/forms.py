from django import forms
from django.core import validators


# One field Clean
# def check_text_length(value):
#    if len(value) < 10:
#        raise forms.ValidationError("TEXT NEEDS TO BE MORE THAN 10 CHARACTERS!")


class FormClass(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField()
    # text = forms.CharField(widget=forms.Textarea, validators=[check_text_length])
    text = forms.CharField()

    # Manual Validator
    # bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput)
    # def clean_bot_catcher(self):
    #     bot_catcher = self.cleaned_data['bot_catcher']
    #
    #     if len(bot_catcher) > 0:
    #         raise forms.ValidationError("BOT!")
    #
    #     return bot_catcher

    # Django Validator
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
    #                             validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']

        if email != verify_email:
            raise forms.ValidationError("Emails don't match!")
