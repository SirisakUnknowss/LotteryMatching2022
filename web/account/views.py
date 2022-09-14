#Django
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt

#Project
from account.models import Account

from .form import AuthenForm

# Create your views here.
@csrf_exempt
def signin(request):
    if request.method == "GET":
        if not(request.user.is_authenticated):
            return render(request, 'base/login.html')
        return render(request, 'base/base.html')
    form = AuthenForm(request.POST)
    if not form.is_valid():
        return redirect(reverse('homepage'))
    try:
        username = form['username'].data
        password = form['password'].data
        account = Account.objects.get(username=username, password=password)
        user = account.user
        login(request, user)
        print(f"username ---- {username}")
        print(f"password ---- {password}")
        return redirect(reverse('homepage'))
    except Account.DoesNotExist:
        context = { 'accountDoesNotExist': 'บัญชีผู้ใช้งานนี้ไม่ถูกต้อง' }
        print(f" ------- {context} ------- ")
        return render(request, 'base/login.html', context)

def homepage(request):
    if not(request.user.is_authenticated):
        return redirect(reverse('signinpage'))
    return render(request, 'base/index.html')

def homepage(request):
    if not(request.user.is_authenticated):
        return redirect(reverse('signinpage'))
    return render(request, 'base/index.html')

def shoppage(request):
    if not(request.user.is_authenticated):
        return redirect(reverse('signinpage'))
    return render(request, 'shop.html')
def userpage(request):
    if not(request.user.is_authenticated):
        return redirect(reverse('userpage'))
    return render(request, 'user.html')

def logoutpage(request):
    logout(request)
    if not(request.user.is_authenticated):
        return redirect(reverse('signinpage'))
    return render(request, 'base/index.html')