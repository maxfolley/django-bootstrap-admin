from django.contrib.admin.forms import AdminAuthenticationForm
from django import forms
from django.contrib.admin.sites import AdminSite

class CustomLoginForm(AdminAuthenticationForm):
  """ Subclass which extends the max length of the username field. """
  username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))

AdminSite.login_form = CustomLoginForm 

