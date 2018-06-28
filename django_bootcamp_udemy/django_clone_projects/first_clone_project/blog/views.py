from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from . import models


class PostCreateView(CreateView):
    fields = ('title', 'text', 'user')
    model = models.Post


class PostListView(ListView):
    model = models.Post
    template_name = 'home.html'
