
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.contrib.auth.models import *
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout
from .forms import ModelForm , CreatePollForm
from .models import Poll
from django.contrib.auth.decorators import login_required

# from poll_project import settings
# from django.core.mail import send_mail

# Create your views here.

def home(request):
    # polls = Poll.objects.all()
    # context = {"polls" : polls}
    return render(request , 'index.html' )

@login_required(login_url='/login')
def view(request):
    polls = Poll.objects.all()
    context = {"polls" : polls}
    return render(request , 'view.html' , context)

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if User.objects.filter(username = username):
            messages.error(request, "Username Aleredy Exist ! Please Try with Some Other Username")
            return redirect(home)
        if User.objects.filter(email = email):
            messages.error(request, "Emaile Aleredy Exist!!")
            return redirect(home)
        if len(username) > 10:
            messages.error(request , "Username must be under 10 characters")
        if pass1 != pass2 :
            messages.error(request , "Password did not match")
        if not username.isalnum():
            messages.error(request , "Username must be alpha-numeric")
            return redirect(home)
        
        myuser = User.objects.create_user (username , email , pass1)
        
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        
        messages.success(request, 'Your Account Has Been Successfully Created')
        return redirect(home)
    return render (request , 'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        user = authenticate (username = username , password = pass1)
        if user is not None:
            login(request , user)
            fname = user.first_name
            return render(request , "create.html" , {'fname' : fname})
        # else:
            # messages.error(request , "Bad Crendentials")
            # return redirect ('home')
    return render(request , 'signin.html')


def signout(request):
    logout(request)
    messages.success(request , "Logged Out Successfully!")
    return redirect('home')

@login_required(login_url='/login')
def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        # question = request.POST['question']
        # option_one = request.POST['option_one']
        # option_two = request.POST['option_two']
        # option_three = request.POST['option_three']
        # option_four = request.POST['option_four']
        # if form.is_valid():
            # poll_form = Poll(question = question , option_one=option_one, option_two=option_two, option_three=option_three, option_four=option_four )
        form.save()
        messages.success(request,"Poll Added SuccessFully")
        return redirect(create)
    else:
        form = CreatePollForm()
        context = {"form" : form}
        return render(request , "create.html" , context)
    
def votepage(request , poll_id):
    poll = Poll.objects.get(pk=poll_id)
    
    if request.method == 'POST':
        selected_option = request.POST['poll']
        
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        elif selected_option == 'option4':
            poll.option_four_count += 1
        else:
            return HttpResponse(request ,"Invalid Form")
        poll.save()
        return redirect(result , poll_id)
    context = {"poll" : poll}
    return render(request , "vote.html" , context)

def result(request , poll_id):
    poll = Poll.objects.get(pk = poll_id)
    context = {"poll" : poll}
    return render(request , "result.html" , context)