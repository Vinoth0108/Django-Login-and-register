# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib.auth.models import User
# from django.contrib import messages
# # Create your views here.

# def index(request):
#    return render(request, 'Myapp/index.html')
# def signup(request):
#     return render(request, 'Myapp/signup.html')
#     if request.method == "POST":
#         username = request.POST['username']
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']

#         myuser = User.objects.create_user(username, email, pass1)
#         myuser.first_name = fname
#         myuser.last_name = lname
#         myuser.save()

#         messages.success(request, "Your Account has been created successfully...!!!")
#         return redirect('signin/')





from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout  # Import necessary authentication modules

# Create your views here.

def index(request):
    return render(request, 'Myapp/index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken...!!!")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered...!!!")
                return redirect('signup')
            else:
                myuser = User.objects.create_user(username, email, pass1)
                myuser.first_name = fname
                myuser.last_name = lname
                myuser.save()

                messages.success(request, "Your Account has been created successfully...!!!")
                return redirect('signin')
        else:
            messages.error(request, "Passwords do not match...!!!")
            return redirect('signup')

    return render(request, 'Myapp/signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(request, username=username, password=pass1)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In...!!!")
            return redirect('index')
        else:
            messages.error(request, "Invalid Credentials...!!!")
            return redirect('signin')

    return render(request, 'Myapp/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out...!!!")
    return redirect('index')





# def signin(request):
#     return render(request, 'Myapp/signin.html')
    
# def signout(request):
#     pass

