from django.views import generic
from django.shortcuts import render


class Home(generic.TemplateView):
	template_name= "account/home.html"

class Login(generic.View):
	def get(self, *args, **kwargs):
		return render(self.request, 'account/login.html')

	def post(self, *args, **kwargs):
		pass	