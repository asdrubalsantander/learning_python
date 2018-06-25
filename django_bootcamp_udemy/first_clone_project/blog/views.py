from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.views import generic
from .forms import ProfileCreationForm


class IndexView(TemplateView):
    template_name = 'index.html'


class SignUp(generic.CreateView):
    form_class = ProfileCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
