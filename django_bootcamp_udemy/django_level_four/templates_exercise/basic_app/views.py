from django.shortcuts import render


def index(request):
    return render(request, 'basic_app/index.html', context=None)


def other(request):
    return render(request, 'basic_app/other.html', context=None)


def relative(request):
    return render(request, 'basic_app/relative_url_templates.html', context=None)

