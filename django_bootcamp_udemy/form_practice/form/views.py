from django.shortcuts import render
from . import forms


def index(request):
    return render(request, 'index.html', context=None)


def form_view(request):
    form = forms.FormClass()
    form_dict = {'form': form}
    return render(request, 'form.html', context=form_dict)
