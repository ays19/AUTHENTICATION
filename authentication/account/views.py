from django.views import generic
from django.shortcuts import render
from .forms import (
    LoginForm
)


class Home(generic.TemplateView):
    template_name = "account/home.html"


class Login(generic.View):
    def get(self, *args, **kwargs):
        form = LoginForm()
        context = {
            "form": form
        }
        return render(self.request, 'account/login.html', context)

    def post(self, *args, **kwargs):
        pass