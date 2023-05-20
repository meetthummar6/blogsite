from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import Signupform
# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class=Signupform
    template_name='registration/register.html'
    success_url=reverse_lazy('login')
