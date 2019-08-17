from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from AdminTestPapers.forms import UserSignUpForm,UserSignUpForm_User_Type,UserLoginForm

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
            # username = singup_form.cleaned_data.get('username')
            # raw_password = signup_form.cleaned_data.get('password1')
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
            else:
                print("Invalid User")
    else:
        signin_form = UserLoginForm()
    return render(request,'signin.html',{'signin_form' : signin_form})
    


