from django.urls import path
from basic_app.views import other, relative

app_name = 'basic_app'

urlpatterns = [
    path('other', other, name="other"),
    path('relative', relative, name="relative"),
]
