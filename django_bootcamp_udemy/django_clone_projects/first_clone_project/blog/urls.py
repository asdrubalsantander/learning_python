from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('draft/', views.DraftListView.as_view(), name='draft'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('<pk>/', views.PostDetailView.as_view(), name='detail'),
    path('update/<pk>', views.PostUpdateView.as_view(), name='update'),
    path('<pk>/comment', views.CommentCreateView.as_view(), name='create_comment'),
]
