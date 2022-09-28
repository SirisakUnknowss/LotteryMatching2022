#Django
from django.shortcuts import redirect
from django.urls import reverse
#Project
from .serializers import SlzShop
from .form import AddShopForm, DeleteShopForm, AddUserForm
from .models import Shop
from base.views import LottListView

# Create your views here.
def addShopApi(request):
    form = AddShopForm(request.POST)
    if not form.is_valid():
        if 'exist' in str(form):
            return 'ชื่อร้านค้านี้มีอยู่แล้ว', False
        if 'incorrect' in str(form):
            return 'ชื่อร้านค้านี้ไม่ถูกต้อง', False
        return 'กรุณากรอกข้อมูลใหม่อีกครั้ง', False
    name = form['name'].data
    Shop.objects.create(name=name)
    return form, True

def addUsernameApi(request):
    form = AddUserForm(request.POST)
    if not form.is_valid():
        if 'shopExist' in str(form):
            return 'ไม่พบร้านค้านี้', False
        if 'usernameExist' in str(form):
            return 'ชื่อผู้ใช้งานนี้มีอยู่แล้ว', False
        if 'incorrect' in str(form):
            return 'ชื่อร้านค้านี้ไม่ถูกต้อง', False
        return 'กรุณากรอกข้อมูลใหม่อีกครั้ง', False
    name = form['name'].data
    Shop.objects.create(name=name)
    return form, True

class ListShow(LottListView):
    """
    """
    queryset = Shop.objects.all()
    serializer_class = SlzShop
    pagination_class = None

def deleteshoppage(request):
    if request.method == "GET":
        return redirect(reverse('shoppage'))
    if not(request.user.is_authenticated):
        return redirect(reverse('homepage'))
    deleteShopApi(request=request)
    return redirect(reverse('shoppage'))

def deleteShopApi(request):
    form =DeleteShopForm(request.POST)
    if not form.is_valid():
        return 'หมายเลขนี้ไม่มีอยู่แล้ว', False
    IDShopDelete = form['IDShopDelete'].data
    Shop.objects.filter(pk=IDShopDelete).delete()
    return form, True