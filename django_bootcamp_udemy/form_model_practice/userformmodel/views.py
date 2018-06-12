from django.shortcuts import render
from .models import User
from .forms import UserForm


def index(request):
    return render(request, "userformmodel/index.html", context=None)


def user_create(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            print("Form VALID")

    return render(request, "userformmodel/user_create.html", {'form':form})


def user_show(request):
    data = User.objects.all().values()
    data_dic = {'users': data}

    return render(request, "userformmodel/user_show.html", context=data_dic)