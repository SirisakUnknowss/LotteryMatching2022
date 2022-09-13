#Django
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from django.contrib.auth import login
from django.contrib.auth.models import User
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
        return render(request, 'base/index.html')
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
        return redirect(reverse('loginpage'))
    return render(request, 'base/index.html')