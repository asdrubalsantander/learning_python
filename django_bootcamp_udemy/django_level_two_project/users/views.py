from django.shortcuts import render
from users.models import Users
# Create your views here.


def users(request):
    data = Users.objects.all().values()
    user_data = {'users': data,
                 'otherdata': 'this is other data'
                 }
    return render(request, 'users.html', context=user_data)
