from django.shortcuts import render


def index(request):
    return render(request, 'basic_app/index.html', context=None)


def other(request):
    context_dict = {'number': 100}
    return render(request, 'basic_app/other.html', context=context_dict)


def relative(request):
    return render(request, 'basic_app/relative_url_templates.html', context=None)
