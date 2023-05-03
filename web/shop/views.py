#Django
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

#Project
from .serializers import SlzShop
from .form import AddShopForm, DeleteShopForm
from .models import Shop
from base.views import LottListView, LottAPIGetView
from numberLottery.models import NumberLottery

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
    NumberLottery.objects.filter(idShop=IDShopDelete).delete()
    Shop.objects.filter(pk=IDShopDelete).delete()
    return form, True

class DeleteShopAll(LottAPIGetView):
    queryset            = Shop.objects.all()
    permission_classes  = [ AllowAny ]
    
    def get(self, request, *args, **kwargs):
        Shop.objects.all().delete()

        return Response({'result': "Delete Shop All Complete"})