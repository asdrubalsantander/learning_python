from django.urls import path
from .views import index_view, signup_view, create_group_view, list_groups_view, detail_group_view


urlpatterns = [
    path('', index_view, name="home"),
    path('signup/', signup_view, name="signup"),
    path('groups/', list_groups_view, name="list_group"),
    path('group/create/', create_group_view, name="create_group"),
    path('group/<pk>/', detail_group_view, name="detail_group"),
]
