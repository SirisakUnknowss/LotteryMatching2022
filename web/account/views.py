#Django
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count
from rest_framework.response import Response

#Project
from base.views import LottAPIGetView
from .models import Account
from .serializers import SlzAccount
from .form import AuthenForm, DeleteUserForm, AddUserForm
from numberLottery.models import NumberLottery, PrototypeNumberLottery
from numberLottery.views import addNumberApi, deleteNumberApi, addManyNumberApi
from shop.models import Shop
from shop.views import addShopApi

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
    
    if not request.user.account.admin:
        return redirect(reverse('addlotterypage'))
    lotteryCount = NumberLottery.objects.all().count
    prototype = PrototypeNumberLottery.objects.filter(matching__isnull=False).values('id').annotate(count=Count('id')).filter(count__gt=1)

    matchNumberCount = prototype.count
    shopCount = Shop.objects.all().count
    context = { 
               'lotteryCount': lotteryCount,
               'matchNumberCount': matchNumberCount,
               'shopCount': shopCount,
            }
    return render(request, 'base/index.html', context)

def shoppage(request):
    if request.method == "GET":
        if not(request.user.is_authenticated) or not request.user.account.admin:
            return redirect(reverse('homepage'))
        return render(request, 'shop.html')
    form, isAddShop = addShopApi(request=request)
    if not isAddShop:
        context = { 'errorAddShop':form }
        return render(request, 'shop.html', context=context)
    context = { 'successAddShop':"เพิ่มข้อมูลสำเร็จ" }
    return render(request, 'shop.html', context=context)

def userpage(request):
    if not request.user.is_authenticated or not request.user.account.admin:
        return redirect(reverse('homepage'))
    form, isAddUser = addUsernameApi(request=request)
    if not isAddUser:
        context = { 'errorAddUser':form }
        return render(request, 'user.html', context=context)
    context = { 'successAddUser':"เพิ่มข้อมูลสำเร็จ" }
    return render(request, 'user.html', context=context)

def shopmatchingpage(request):
    if request.method == "GET":
        if (request.user.is_authenticated) or request.user.account.admin:
            return render(request, 'shopMatching.html')
    return redirect(reverse('homepage'))

def addlotterypage(request):
    if request.method == "GET":
        if not(request.user.is_authenticated):
            return redirect(reverse('homepage'))
        return render(request, 'addLottery.html')
    
    statusAdd = request.POST['statusAdd']
    form = ""
    isAddNumber = False
    if statusAdd == "one":
        form, isAddNumber = addNumberApi(request=request)
    elif statusAdd == "many":
        form, isAddNumber = addManyNumberApi(request=request)
    else:
        return render(request, 'addLottery.html')
    context = form
    if not isAddNumber:
        return render(request, 'addLottery.html', context=context)
    context['successAddNumber'] = "เพิ่มข้อมูลสำเร็จ"
    return render(request, 'addLottery.html', context=context)

def deletelotterypage(request):
    if request.method == "GET":
        return redirect(reverse('addlotterypage'))
    if not(request.user.is_authenticated):
        return redirect(reverse('homepage'))
    deleteNumberApi(request=request)
    return redirect(reverse('addlotterypage'))

def logoutpage(request):
    logout(request)
    return redirect(reverse('homepage'))

class ListAccount(LottAPIGetView):
    
    queryset = Account.objects.all()
    serializer_class = SlzAccount
    pagination_class = None
    
    def get(self, request, *args, **kwargs):
        queryset = Account.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        self.response["result"] = serializer.data
        return Response(self.response)

def deleteuserpage(request):
    if request.method == "GET":
        return redirect(reverse('userpage'))
    if not(request.user.is_authenticated):
        return redirect(reverse('homepage'))
    deleteUserApi(request=request)
    return redirect(reverse('userpage'))

def deleteUserApi(request):
    form =DeleteUserForm(request.POST)
    if not form.is_valid():
        return 'ผู้ใช้งานนี้ไม่มีอยู่แล้ว', False
    IDUserDelete = form['IDUserDelete'].data
    Account.objects.filter(pk=IDUserDelete).delete()
    return form, True

def addUsernameApi(request):
    form = AddUserForm(request.POST)
    if not form.is_valid():
        if 'usernameExist' in str(form):
            return 'ชื่อผู้ใช้งานนี้มีอยู่แล้ว', False
        if 'incorrect' in str(form):
            return 'ชื่อร้านค้านี้ไม่ถูกต้อง', False
        return 'กรุณากรอกข้อมูลใหม่อีกครั้ง', False
    inputName = form['inputName'].data
    inputUsername = form['inputUsername'].data
    inputPassword = form['inputPassword'].data
    user = Account.createUser()
    Account.objects.create(name=inputName, username=inputUsername, password=inputPassword, user=user)
    return form, True