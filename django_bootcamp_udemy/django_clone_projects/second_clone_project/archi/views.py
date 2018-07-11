from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import UserCreateForm, GroupCreateForm


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
            group = form.save(commit=False)
            user = request.user
            group.user = user
            group.save()
            return redirect('home')
    else:
        form = GroupCreateForm()
        return render(request, 'group_form.html', {'form': form})