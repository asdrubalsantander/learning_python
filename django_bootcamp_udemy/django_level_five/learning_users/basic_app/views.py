from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    return render(request, 'basic_app/index.html', context=None)


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    register_dic = {
        'registered': registered,
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'basic_app/registration.html', context=register_dic)


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print('LOGIN FAILED')
            return HttpResponse("Invalid Login")

    else:
        return render(request, 'basic_app/login.html', context=None)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def special(request):
    return HttpResponse("You are logged in")
