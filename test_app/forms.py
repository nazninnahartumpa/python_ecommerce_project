from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class ContactForm(forms.Form):
	name = forms.CharField(max_length=255,
							widget=forms.TextInput(
								attrs={
									"class": "form-control",
									"placeholder": "Enter Your Username"
								}))
	email = forms.EmailField(widget=forms.EmailInput(
								attrs={
									"class": "form-control",
									"placeholder": "Enter Your Email"
								}))
	content = forms.CharField(max_length=255,
								widget=forms.Textarea(
								attrs={
									"class": "form-control",
									"placeholder": "Enter Your Message"
								}))


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
	username = forms.CharField(max_length=255,
							widget=forms.TextInput(
								attrs={
									"class": "form-control",
									"placeholder": "Enter Your Username"
								}))
	email = forms.EmailField(max_length=255,
							widget=forms.EmailInput(
								attrs={
									"class": "form-control",
									"placeholder": "Enter Your Email"
								}))
	password = forms.CharField(max_length=255, widget=forms.PasswordInput(
								attrs={
									"class": "form-control",
									"placeholder": "Enter Your Password"
								}))
	password2 = forms.CharField(max_length=255, label="Confirm Password",widget=forms.PasswordInput(
								attrs={
									"class": "form-control",
									"placeholder": "Enter Your Password Again"
								}))

	def clean_username(self):
		username = self.cleaned_data.get('username')
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("Username is taken!")
		else:
			return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("Email is taken!")
		else:
			return email

	def clean(self):
		data = self.cleaned_data
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if password2 != password:
			raise forms.ValidationError("Password did not match!")
		else:
			return data
