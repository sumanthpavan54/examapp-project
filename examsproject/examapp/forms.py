from django import forms
from django.contrib.auth.models import User
from examapp.models import FirstQuestion
from examapp.models import SecondQuestion
from examapp.models import ThirdQuestion
from examapp.models import FourthQuestion
from examapp.models import FifthQuestion

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']
class FirstQuestionForm(forms.ModelForm):
    class Meta:
        model=FirstQuestion
        fields=['answer',]

class SecondQuestionForm(forms.ModelForm):
    class Meta:
        model=SecondQuestion
        fields=['answer',]

class ThirdQuestionForm(forms.ModelForm):
    class Meta:
        model=ThirdQuestion
        fields=['answer',]

class FourthQuestionForm(forms.ModelForm):
    class Meta:
        model=FourthQuestion
        fields=['answer',]

class FifthQuestionForm(forms.ModelForm):
    class Meta:
        model=FifthQuestion
        fields=['answer',]
