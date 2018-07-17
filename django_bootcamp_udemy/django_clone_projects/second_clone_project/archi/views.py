from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import UserCreateForm, GroupCreateForm, PostCreateForm
from .models import Topic, Post
from django.forms.models import model_to_dict
from pprint import pprint
from django.contrib.auth.decorators import login_required


def index_view(request):
    return render(request, template_name='index.html', context=None)


def signup_view(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreateForm()
    return render(request, template_name='signup.html', context={'form': form})


@login_required
def create_group_view(request):
    if request.method == "POST":
        form = GroupCreateForm(request.POST)
        if form.is_valid:
            group = form.save()
            user = request.user
            group.user.add(user)
            return redirect('home')
    else:
        form = GroupCreateForm()
        return render(request, 'group_form.html', {'form': form})


def list_groups_view(request):
    groups = Topic.objects.all()
    return render(request, 'group_list.html', context={'group_dict': groups})


def detail_group_view(request, pk):
    group_detail = Topic.objects.get(pk=pk)
    user_is_member = False
    if request.user.is_authenticated:
        user_is_member = True if request.user.topic_set.filter(pk=pk).exists() else False
    return render(request, 'group_detail.html', context={'group': group_detail, 'member': user_is_member})


@login_required
def join_group_view(request, pk):
    user_is_member = False
    if request.method == "POST":
        group = Topic.objects.get(pk=pk)
        if 'leave_group' in request.POST:
            group.user.remove(request.user)
        elif 'join_group' in request.POST:
            group.user.add(request.user)
            user_is_member = True
    return render(request, 'group_detail.html', context={'group': group, 'member': user_is_member})


@login_required
def create_post_view(request):
    if request.method == "POST":
        form = PostCreateForm(request.user, request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('detail_group', pk=post.topic.pk)
    else:
        form = PostCreateForm(request.user)
        return render(request, 'post_form.html', {'form': form})


def detail_post_view(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})
