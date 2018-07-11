from django.urls import path
from .views import index_view, signup_view, create_group_view


urlpatterns = [
    path('', index_view, name="home"),
    path('signup/', signup_view, name="signup"),
    path('group/create/', create_group_view, name="create_group")
]
