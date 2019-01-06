from django.shortcuts import render
from examapp import forms
from examapp.forms import SignUpForm
from django.http import HttpResponseRedirect
from examapp.forms import FirstQuestionForm
from examapp.forms import SecondQuestionForm
from examapp.forms import ThirdQuestionForm
from examapp.forms import FourthQuestionForm
from examapp.forms import FifthQuestionForm


from examapp.models import FirstQuestion
from examapp.models import SecondQuestion
from examapp.models import ThirdQuestion
from examapp.models import FourthQuestion
from examapp.models import FifthQuestion
from django.contrib.auth.models import User

# Create your views here.
def python_view(request):
    return render(request, 'examapp/python.html')

def java_view(request):
    return render(request,'examapp/java.html')

def aptitude_view(request):
    return render(request,'examapp/aptitude.html')

def home_view(request):
    return render(request,'examapp/home.html')

def first_view(request):
    return render(request, 'examapp/first.html')

def thanks_view(request):


    return render(request, 'examapp/thanks.html')
def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')

    return render(request, 'examapp/signup.html', {'form':form})

def firstquestion(request):
    form=forms.FirstQuestionForm()
    if request.method=='POST':
        form=forms.FirstQuestionForm(request.POST)
        if form.is_valid():

            solution=form.cleaned_data['answer']
            if solution==1:

                name=request.user.username
                First=FirstQuestion(answer=solution,marks=2,username=name)
                First.save()
            else:
                name=request.user.username
                First=FirstQuestion(answer=solution,marks=0,username=name)
                First.save()
            return render(request, 'examapp/Firstquestionsubmit.html')
    return render(request,'examapp/firstquestion.html',{'form':form})
def Secondquestion(request):
    form=forms.SecondQuestionForm()
    if request.method=='POST':
        form=forms.SecondQuestionForm(request.POST)
        if form.is_valid():

            solution=form.cleaned_data['answer']
            if solution==2:

                name=request.user.username
                Second=SecondQuestion(answer=solution,marks=2,username=name)
                Second.save()
            else:
                name=request.user.username
                Second=SecondQuestion(answer=solution,marks=0,username=name)
                Second.save()

            return render(request, 'examapp/Secondquestionsubmit.html')
    return render(request,'examapp/Secondquestion.html',{'form':form})
def Thirdquestion(request):
    form=forms.ThirdQuestionForm()
    if request.method=='POST':
        form=forms.ThirdQuestionForm(request.POST)
        if form.is_valid():

            solution=form.cleaned_data['answer']
            if solution==3:

                name=request.user.username
                Third=ThirdQuestion(answer=solution,marks=2,username=name)
                Third.save()
            else:
                name=request.user.username
                Third=ThirdQuestion(answer=solution,marks=0,username=name)
                Third.save()

            return render(request, 'examapp/Thirdquestionsubmit.html')
    return render(request,'examapp/Thirdquestion.html',{'form':form})

def Fourthquestion(request):
    form=forms.FourthQuestionForm()
    if request.method=='POST':
        form=forms.FourthQuestionForm(request.POST)
        if form.is_valid():

            solution=form.cleaned_data['answer']
            name=request.user.username
            Fourth=FourthQuestion(answer=solution,marks=0,username=name)
            Fourth.save()

            return render(request, 'examapp/Fourthquestionsubmit.html')
    return render(request,'examapp/Fourthquestion.html',{'form':form})

def Fifthquestion(request):
    form=forms.FifthQuestionForm()
    if request.method=='POST':
        form=forms.FifthQuestionForm(request.POST)
        if form.is_valid():

            solution=form.cleaned_data['answer']
            name=request.user.username
            Fifth=FifthQuestion(answer=solution,marks=0,username=name)
            Fifth.save()

            return render(request, 'examapp/Fifthquestionsubmit.html')
    return render(request,'examapp/Fifthquestion.html',{'form':form})



def Totalscore(request):

    name=request.user.username
    mark1=FirstQuestion.objects.get(username=name)
    m1=mark1.marks
    mark2=SecondQuestion.objects.get(username=name)
    m2=mark2.marks
    mark3=ThirdQuestion.objects.get(username=name)
    m3=mark3.marks
    mark4=FourthQuestion.objects.get(username=name)
    m4=mark4.marks
    mark5=FifthQuestion.objects.get(username=name)
    m5=mark5.marks
    m6=m1+m2+m3+m4+m5
    return render(request,'examapp/totalscore.html', {'m':m6})
