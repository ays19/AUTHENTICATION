from django import forms
from django.views import generic
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy


from .forms import (
    LoginForm,
        
)


class Home(LoginRequiredMixin, generic.TemplateView):
    login_url = 'login'
    template_name = "account/home.html"


class Login(generic.View):
    def get(self, *args, **kwargs):
        form = LoginForm()
        context = {
            "form": form
        }
        return render(self.request, 'account/login.html', context)

    def post(self, *args, **kwargs):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(self.request, username=username, password=password)
            if user is not None:
                login(self.request, user)
                return redirect('home')  # Redirect to home after login
            else:
                form.add_error(None, "Invalid username or password")
        context = {
            "form": form
        }
        return render(self.request, 'account/login.html', context)