from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	firstname = forms.CharField()
	lastname = forms.CharField()
	phoneno = forms.IntegerField()


	class Meta:
		model = User
		fields = ['username', 'email', 'firstname', 'lastname', 'phoneno', 'password1', 'password2']
