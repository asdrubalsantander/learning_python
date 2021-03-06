from django.urls import path
from .views import index_view, signup_view, create_group_view, list_groups_view, \
    detail_group_view, join_group_view, create_post_view, detail_post_view, user_post_view


urlpatterns = [
    path('', index_view, name="home"),
    path('signup/', signup_view, name="signup"),
    path('groups/', list_groups_view, name="list_group"),
    path('group/create/', create_group_view, name="create_group"),
    path('group/<pk>/', detail_group_view, name="detail_group"),
    path('group/<pk>/join', join_group_view, name="join_group"),
    path('post/create', create_post_view, name="create_post"),
    path('post/<pk>', detail_post_view, name="detail_post"),
    path('post/by/<username>', user_post_view, name="user_post")
]
