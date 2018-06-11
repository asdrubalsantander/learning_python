from django.shortcuts import render
from . import forms


def index(request):
    return render(request, 'index.html', context=None)


def form_view(request):
    form = forms.FormClass()

    if request.method == "POST":
        form = forms.FormClass(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])

    return render(request, 'form.html', {'form':form})

