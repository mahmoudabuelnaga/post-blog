from django.shortcuts import render
from .forms import Register_form
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User


class User_register(CreateView):
    form_class = Register_form
    template_name = 'registration/register.html'
    success_url = 'login'