from django import forms
from AdminTestPapers.models import SiteUser
from django.contrib.auth.models import User

class UserSignUpForm_User_Type(forms.ModelForm):
  class Meta:
    model = SiteUser
    fields = ['user_type']

class UserSignUpForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput())
  class Meta:
    model = User
    fields = ['username','password']
