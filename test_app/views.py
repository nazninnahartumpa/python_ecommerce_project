from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from .forms import *

############# Index Page ##################
class IndexView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		return context

############# Contact Page ##################
class ContactPageView(View):

	def get(self, request):
		contact_form = ContactForm()
		context = {
			'form': contact_form
		}			
		return render(request, 'contact/contact.html', context)

	def post(self, request):
		contact_form = ContactForm(request.POST or None)
		context = {
			'form': contact_form
		}

		if contact_form.is_valid():
			print(contact_form.cleaned_data)
			print(request.POST.get("email"))
			print(request.POST.get("content"))

		return render(request, 'contact/contact.html', context)

############# Login Page ##################
class LoginPage(View):
	# template_name = 'auth/login.html'
	# form_class = LoginForm
	# success_url = 'login/'

	def get(self, request):
		form = LoginForm()
		context = {
			"form": form
		}
		return render(request, 'auth/login.html', context)

	def post(self, request):
		form = LoginForm(request.POST or None)
		context = {
			"form": form
			}
		#print("User logged in")
		#print(user.is_authenticated())
		if form.is_valid():
			print(form.cleaned_data)
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")

			user = authenticate(request, username=username, password=password)
			print(user)
			#print(self.user.is_authenticated())
			if user is not None:
				login(request, user)
				
				return redirect("/login")
			else:
				print("error!")

		return render(request, 'auth/login.html', context)

############# Registration Page ##################
User = get_user_model()
class RegisterPage(View):
	def get(self, request):
		form = RegisterForm()
		context = {
			"form": form
		}
		return render(request, 'auth/register.html', context)

	def post(self, request):
		form = RegisterForm(request.POST or None)
		context = {
			'form': form
		}

		if form.is_valid():
			print(form.cleaned_data)
			username = form.cleaned_data.get("username")
			email = form.cleaned_data.get("email")
			password = form.cleaned_data.get("password")
			new_user = User.objects.create_user(username, email, password)
			print(new_user)

		return render(request, 'auth/register.html', context)

