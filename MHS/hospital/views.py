from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def About(request):
    return render(request, 'about.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login.html')
    return render(request, 'index.html')

def Login(request):
    if request.method=='POST':
        user_name = request.POST['uname']
        pass_word = request.POST['pwd']
        user = authenticate(username=user_name,password=pass_word)

    if not request.user.is_staff:
        return redirect('login.html')
    return render(request, 'index.html')

def Logout(request):
    if not request.user.is_staff:
        return redirect('login.html')
    logout(request, 'index.html')