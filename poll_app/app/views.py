from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreatePollForm
from .models import poll


def home(request):
    return render(request, "app/index.html")


def homepage(request):
    polls = poll.objects.all()
    context = {'polls': polls}
    return render(request, "app/hp.html", context)


def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = CreatePollForm()
    context = {'form': form}
    return render(request, "app/create.html", context)


def vote(request, poll_id):
    polls = poll.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']

        if selected_option == 'option1':
            polls.option1_count += 1
        elif selected_option == 'option2':
            polls.option2_count += 1
        elif selected_option == 'option3':
            polls.option3_count += 1
        elif selected_option == 'option4':
            polls.option4_count += 1
        else:
            return HttpResponse(600, 'Invalid form')

        polls.save()

        return redirect('result', poll_id)

    context = {'polls': polls}
    return render(request, 'app/vote.html', context)


def result(request, poll_id):
    polls = poll.objects.get(pk=poll_id)
    context = {'polls': polls}
    return render(request, "app/result.html", context)


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if len(username) > 10:
            messages.error(request, "Username must not exceed 10 characters.!")
            return redirect('signup')

        if pass1 != pass2:
            messages.error(request, "Passwords doesn't match")
            return redirect('signup')

        if not username.isalnum():
            messages.error(request, "Username must contain numbers and characters as well. !")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your account has been created succesfully.")
        return redirect('signin')

    return render(request, "app/signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "app/index.html")
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('homepage')

    return render(request, "app/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "logged out successfully.")
    return redirect('home')
