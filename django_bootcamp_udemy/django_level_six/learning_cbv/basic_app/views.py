from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


class index_view(View):
    def get(self, request):
        return HttpResponse('CLASS VIEW')
