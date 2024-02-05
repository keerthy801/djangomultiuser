from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app1.models import CustomUser

# Create your views here.

def home(request):
    return render(request,"home.html")

def adminhome(request):
    return render(request,"adminhome.html")

def studenthome(request):
    return render(request,"studenthome.html")

def teacherhome(request):
    return render(request,"teacherhome.html")

def adminsignup(request):
    if(request.method == "POST"):
        us = request.POST['us']
        ps = request.POST['ps']
        cp = request.POST['cp']
        fn = request.POST['fn']
        ln = request.POST['ln']
        em = request.POST['em']
        ph = request.POST['ph']
        pl = request.POST['pl']
    # phonenumber&place

        if (ps == cp):
            user = CustomUser.objects.create_user(username=us, password=ps, first_name=fn, last_name=ln, email=em, phone=ph,
                                                  place=pl)
            user.is_admin=True
            user.save()
            return home(request)

    return render(request,'adminsignup.html')

def studentsignup(request):
    if(request.method == "POST"):
        us = request.POST['us']
        ps = request.POST['ps']
        cp = request.POST['cp']
        fn = request.POST['fn']
        ln = request.POST['ln']
        em = request.POST['em']
        ph = request.POST['ph']
        pl = request.POST['pl']
        # phonenumber&place

        if (ps == cp):
            user = CustomUser.objects.create_user(username=us, password=ps, first_name=fn, last_name=ln, email=em, phone=ph,
                                                  place=pl)
            user.is_student = True
            user.save()
            return home(request)
    return render(request,'studentsignup.html')

def teachersignup(request):
    if(request.method == "POST"):
        us = request.POST['us']
        ps = request.POST['ps']
        cp = request.POST['cp']
        fn = request.POST['fn']
        ln = request.POST['ln']
        em = request.POST['em']
        ph = request.POST['ph']
        pl = request.POST['pl']
    # phonenumber&place

        if (ps == cp):
            user = CustomUser.objects.create_user(username=us, password=ps, first_name=fn, last_name=ln, email=em, phone=ph,
                                                  place=pl)
            user.is_teacher = True
            user.save()
            return home(request)
    return render(request,'teachersignup.html')


def user_login(request):
    if (request.method == "POST"):
        us = request.POST['us']
        ps = request.POST['ps']
        print(us)
        user = authenticate(username=us, password=ps)
        if user and user.is_admin==True:
            login(request, user)
            print(us)
            return redirect('app1:adminhome')
        elif user and user.is_teacher==True:
            login(request, user)
            return teacherhome(request)
        elif user and user.is_student==True:
            login(request, user)
            return studenthome(request)
        else:
            return HttpResponse("Invalid Credentials")
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect("app1:login")