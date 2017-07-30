from django import forms
from django.contrib.auth.models import User
from app5.models import UserProfileInfo


class UserForm(forms.ModelForm):
	password = forms.CharField(widget =  forms.PasswordInput())

	class Meta():
		model = User
		fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
	class Meta():
		model = UserProfileInfo
		fields = ('desc', 'portfolio_site', 'status', 'profilepic')