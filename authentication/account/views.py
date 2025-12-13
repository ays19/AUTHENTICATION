from django import forms
from django.views import generic
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy


from .mixins import (
    LogoutRequiredMixin,
)

from .forms import (
    LoginForm,
        
)


class Home(LoginRequiredMixin, generic.TemplateView):
    Login_url = 'login'
    template_name = "account/home.html"


class Login(LogoutRequiredMixin,generic.View):
    def get(self, *args, **kwargs):
        form = LoginForm()
        context = {
            "form": form
        }
        return render(self.request, 'account/login.html', context)
    
def post(self, *args, **kwargs):
		form = LoginForm(self.request.POST)
		if form.is_valid():
			user = authenticate(
					self.request,
					username=form.cleaned_data.get('username'),
					password=form.cleaned_data.get('password')
				)
			if user:
					login(self.request, user)
					return redirect('home')
			else:	
				forms.ValidationError("Incorrect password")
				return redirect('login')
		return render(self.request, 'account/login.html', {"form": form})
    
class Logout(generic.View):
    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect('login')    

   