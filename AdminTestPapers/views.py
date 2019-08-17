from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from AdminTestPapers.forms import UserSignUpForm, UserSignUpForm_User_Type, UserLoginForm, QuestionForm

def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        signup_form = UserSignUpForm(data = request.POST)
        signup_form_user_type = UserSignUpForm_User_Type(data = request.POST)
        if signup_form.is_valid() and signup_form_user_type.is_valid():
            user = signup_form.save()
            user.set_password(user.password)
            user.save()
            user_type = signup_form_user_type.save(commit = False)
            user_type.user = user
            user_type.save() 
            return redirect('/signin')
        else:
            print("Error In Filling Up The Form")
    else:
        signup_form = UserSignUpForm()
        signup_form_user_type = UserSignUpForm_User_Type()
    return render(request, 'signup.html', {'signup_form': signup_form,'signup_form_user_type': signup_form_user_type})

def signin(request):
    if request.method == "POST":
        signin_form = UserLoginForm(data = request.POST)
        if signin_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            theUser = authenticate(request, username=username, password=password)
            if theUser is not None:
                login(request,theUser)
                print("Success")
                return redirect('/')
            else:
                print("Invalid User")
                return redirect('/signin')
    else:
        signin_form = UserLoginForm()
    return render(request,'signin.html',{'signin_form' : signin_form})
    

def question(request):
    if (request.user.is_authenticated):
        user = request.user
        print(user)
        if (user.profile and user.profile.user_type == 'T'):
            profile = user.profile
            if (request.method == "POST"):
                question_form = QuestionForm(data=request.POST)
                if question_form.is_valid():
                    question = question_form.save(commit=False)
                    teacher = profile
                    teacher.user = user
                    # teacher.save()
                    question.teacher = teacher
                    question.save()
                    print("Question added!")
                    return redirect('/', {'question': True})
                else:
                    print("Error Filling the Form!")
            else:
                question_form = QuestionForm()
            return render(request, 'question.html', {'question_form': question_form})
        else:
            return HttpResponse("Invalid Request")
    else:
        return redirect('/signin')
