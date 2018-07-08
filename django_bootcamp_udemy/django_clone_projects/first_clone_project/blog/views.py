from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from . import models
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login'
    redirect_field_name = 'home'
    fields = ('title', 'text', 'user')
    model = models.Post


class PostListView(ListView):
    model = models.Post
    template_name = 'home.html'

    def get_queryset(self):
        # return models.Post.objects.filter(date_created__lte=timezone.now()).order_by('-date_created')
        return models.Post.objects.filter(title__startswith='My')


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


def comment_create(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})


def comment_approve(request, pk):
    comment = get_object_or_404(models.Comment, pk=pk)
    comment.approve_comment()
    return redirect('blog:detail', pk=comment.post.pk)


def comment_delete(request, pk):
    comment = get_object_or_404(models.Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:detail', pk=post_pk)