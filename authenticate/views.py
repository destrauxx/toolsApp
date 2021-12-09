from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.password_validation import UserAttributeSimilarityValidator

from .forms import RegisterForm
# Create your views here.

class RegistrationView(CreateView):
    form_class = RegisterForm
    template_name = 'authenticate/register.html'
    success_url = reverse_lazy('login')

class LoginView(LoginView):
    template_name = 'authenticate/login.html'
    success_url = reverse_lazy('homepage')

class LogoutView(LogoutView):
    redirect_field_name = reverse_lazy("homepage")
    template_name = "index.html"