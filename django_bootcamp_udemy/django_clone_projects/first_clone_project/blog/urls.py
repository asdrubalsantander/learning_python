from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('draft/', views.DraftListView.as_view(), name='draft'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('<pk>/', views.PostDetailView.as_view(), name='detail'),
    path('update/<pk>', views.PostUpdateView.as_view(), name='update'),
    path('<pk>/comment', views.comment_create, name='create_comment'),
    path('<pk>/comment/approve', views.comment_approve, name='approve_comment'),
    path('<pk>/comment/delete', views.comment_delete, name='delete_comment'),
]
