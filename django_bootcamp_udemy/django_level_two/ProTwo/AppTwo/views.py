from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(response):
    my_names = {'django_var': "From views.py"}
    return render(response, 'index.html', context=my_names)


def help_me(response):
    return render(response, 'help-me.html', context=None)
