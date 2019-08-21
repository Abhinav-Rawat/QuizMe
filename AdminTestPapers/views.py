from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from AdminTestPapers.forms import UserSignUpForm, UserSignUpForm_User_Type, UserLoginForm, QuestionForm, PaperForm
from datetime import datetime
from AdminTestPapers.models import Question, QuestionPaper, MarksFromTheQuestion


def home(request):
    papers = QuestionPaper.objects.order_by("pub_date")[:10]
    return render(request,'home.html', {'papers': papers})

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
        if (request.user.is_authenticated):
            return HttpResponse("<h2>You are already logged in.</h2><p>Log out to log in from another account.</p>")
        signin_form = UserLoginForm()
    return render(request,'signin.html',{'signin_form' : signin_form})


def logout_view(request):
    logout(request)
    return redirect('/')


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
                    question.created_at = datetime.now()
                    question.save()
                    print("Question added!")
                    return HttpResponse("Question Added")
                else:
                    return HttpResponse("Error Filling the Form!")
            elif (request.method == 'GET'):
                pid = request.GET["id"]
                print("pid", pid)
            question_form = QuestionForm(initial={'q_paper': pid})
            return render(request, 'question.html', {'question_form': question_form})
        else:
            return HttpResponse("Invalid Request")
    else:
        return redirect('/signin')


def makePaper(request):
    if (request.user.is_authenticated):
        user = request.user
        print(user)
        if (user.profile and user.profile.user_type == 'T'):
            profile = user.profile

            if request.method == "POST":
                paper_form = PaperForm(data=request.POST)
                if paper_form.is_valid():
                    paper = paper_form.save(commit=False)
                    paper.pub_date = datetime.now()
                    teacher = profile
                    teacher.user = user
                    paper.teacher = teacher
                    paper.save()
                    # link = "question/"+str(paper.id)
                    # print("link", link)
                    print("id", paper.id)
                    return render(request, 'make_ques.html', {'paper': paper, 'temp': "Hello World"})
                else:
                    print("Error Filling the Form!")
                    return HttpResponse("Error Filling the Form!")

            else:
                paper_form = PaperForm()
                return render(request,"paper_maker.html",{'paper_form': paper_form})

        else:
            return HttpResponse("Invalid Request")
    else:
        return redirect('/signin')


def allTests(request):
    if request.user.is_authenticated:
        user = request.user
        if user.profile and user.profile.user_type == "S":
            profile = user.profile
            papers = QuestionPaper.objects.order_by("pub_date")
            return render(request, 'alltests.html', {'papers': papers})
        else:
            return HttpResponse("Login as student to see all papers!")
    else:
        return redirect('/signin')



def takeTest(request):
    if request.user.is_authenticated:
        user = request.user
        if user.profile and user.profile.user_type == "S":
            profile = user.profile
            pid = request.GET["id"]
            questionList = Question.objects.filter(q_paper=pid)
            q_paper = QuestionPaper.objects.get(id=pid)
            print(pid)
            print("paper:", q_paper.title_text)
            return render(request,"testOngoing.html",{"paperID": str(pid), "questions": questionList, "paper": q_paper})
        else:
            return HttpResponse("Only A Student Can Give Tests")
    else:
        return redirect('/signin')


def paper_done(request):
    if request.user.is_authenticated:
        user = request.user
        if user.profile and user.profile.user_type == "S":
            profile = user.profile
            if request.method == "GET":
                return render("Invalid Action")
            elif request.method == "POST":
                paper_id = request.POST["paper_id"]
                current_paper = QuestionPaper.objects.get(id = int(paper_id))
                questionList = Question.objects.filter(q_paper = int(paper_id))
                for q in questionList:
                    newObj = MarksFromTheQuestion()
                    newObj.test = current_paper
                    newObj.student = profile
                    newObj.question = q
                    verifyObjList = MarksFromTheQuestion.objects.filter(student=profile.id, test=paper_id, question=q.id)
                    verifyObj = None
                    if verifyObjList:
                        verifyObj = verifyObjList[0]
                    if q.ans_text == request.POST[str(q.id)]:
                        newObj.correct = True
                    if verifyObj:
                        verifyObj.correct = newObj.correct
                        verifyObj.save()
                    else:
                        newObj.save()

                theList = MarksFromTheQuestion.objects.filter(student = profile.id, test = paper_id)
                correct = 0
                total = 0
                for q in theList:
                    total += 1
                    if q.correct:
                        correct += 1
                return HttpResponse("You Got "+str(correct)+" Out Of "+str(total))
        else:
            return HttpResponse("Only A Student Can Give Tests")
    else:
        return redirect('\signin')
