from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    redirect_field_name = 'home'
    fields = ('title', 'text', 'user')
    model = models.Post


class PostListView(ListView):
    model = models.Post
    template_name = 'home.html'


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login'
    redirect_field_name = 'draft'
    model = models.Post
    template_name = 'blog/draft_list.html'


class PostDetailView(DetailView):
    model = models.Post
    template_name = 'blog/post_detail.html'


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login'
    redirect_field_name = 'home'
    fields = ('title', 'text', 'is_published')
    model = models.Post


class CommentCreateView(CreateView):
    fields = ('username', 'text')
    model = models.Comment

    def form_valid(self, form):
        form.instance.post = models.Post.objects.get(id=1)
        return super(CommentCreateView, self).form_valid(form)
