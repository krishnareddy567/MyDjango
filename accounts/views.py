from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.

def register(request):

    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        username=request.POST['username']

        if(password1==password2):
            if User.objects.filter(username=username).exists():
                print("Username taken")
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=firstname,last_name=lastname)
                user.save();
                print("User was Created.")
        else:
            print("Password not matching")
        return redirect('/')
    return render(request,'register.html')
