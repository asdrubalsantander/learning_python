from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import UserCreateForm, GroupCreateForm
from .models import Topic
from django.forms.models import model_to_dict
from pprint import pprint


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
