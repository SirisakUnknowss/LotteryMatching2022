#Django
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt

#Project
from account.models import Account
from numberLottery.models import NumberLottery
from numberLottery.views import addNumberApi
from shop.models import Shop
from shop.views import addShopApi
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
        return redirect(reverse('homepage'))
    except Account.DoesNotExist:
        context = { 'accountDoesNotExist': 'บัญชีผู้ใช้งานนี้ไม่ถูกต้อง' }
        return render(request, 'base/login.html', context)

def homepage(request):
    if not(request.user.is_authenticated):
        return redirect(reverse('signinpage'))
    lotteryCount = NumberLottery.objects.all().count
    matchNumberCount = NumberLottery.objects.all().count
    shopCount = Shop.objects.all().count
    context = { 
               'lotteryCount': lotteryCount,
               'matchNumberCount': matchNumberCount,
               'shopCount': shopCount,
            }
    return render(request, 'base/index.html', context)

def shoppage(request):
    if request.method == "GET":
        if not(request.user.is_authenticated):
            return redirect(reverse('signinpage'))
        return render(request, 'shop.html')
    form, isAddShop = addShopApi(request=request)
    if not isAddShop:
        context = { 'errorAddShop':form }
        return render(request, 'shop.html', context=context)
    context = { 'successAddShop':"เพิ่มข้อมูลสำเร็จ" }
    return render(request, 'shop.html', context=context)

def userpage(request):
    if not(request.user.is_authenticated):
        return redirect(reverse('homepage'))
    return render(request, 'user.html')

def addlotterypage(request):
    if request.method == "GET":
        if not(request.user.is_authenticated):
            return redirect(reverse('homepage'))
        return render(request, 'addLottery.html')
    form, isAddShop = addNumberApi(request=request)
    if not isAddShop:
        context = { 'errorAddNumber':form }
        return render(request, 'addLottery.html', context=context)
    context = { 'successAddNumber':"เพิ่มข้อมูลสำเร็จ" }
    return render(request, 'addLottery.html', context=context)

def logoutpage(request):
    logout(request)
    return redirect(reverse('homepage'))