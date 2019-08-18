from django import forms
from AdminTestPapers.models import SiteUser, Question, QuestionPaper
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

class UserLoginForm(forms.Form):
  username = forms.CharField(widget = forms.TextInput())
  password = forms.CharField(widget = forms.PasswordInput())


class QuestionForm(forms.ModelForm):
  class Meta:
    model = Question
    exclude = ['teacher', 'created_at',]  


class PaperForm(forms.ModelForm):
  class Meta:
    model = QuestionPaper
    fields = ('title_text',)