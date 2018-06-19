from django.urls import path
from . import views


urlpatterns = [
    path('user-create/', views.user_create),
    path('user-show/', views.user_show),
]