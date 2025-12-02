from django.views import generic
from django.shortcuts import render


class Home(generic.TemplateView):
	template_name= "account/home.html"