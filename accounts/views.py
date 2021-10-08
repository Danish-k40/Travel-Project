from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:            #registered username and password
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid details')
            return redirect('login')

    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        # ------- password checking, email, user name checking ---------------
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save()
                print("user registered")

        return redirect('/')      # ('/') means redirect to previous page
    else:
        return render(request, 'registration.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


     # return render(request, 'registration.html')
