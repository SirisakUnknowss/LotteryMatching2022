#Django
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework.response import Response
from django.db.models import Count
#Project
from base.views import LottAPIGetView
from account.models import Account
from .models import NumberLottery, PrototypeNumberLottery
from .form import DeleteNumberLotteryForm
from .serializers import SlzListNumber

# Create your views here.
class ListNumberLotteryMatching(LottAPIGetView):

    queryset = NumberLottery.objects.all()
    serializer_class = SlzListNumber
    pagination_class = None
    
    def get(self, request, *args, **kwargs):
        prototype = PrototypeNumberLottery.objects.filter(matching__isnull=False).values('id', 'numberLottery').annotate(count=Count('id')).filter(count__gt=1)
        listNumber = []
        for numberMatching in prototype:
            listNumber.append(numberMatching['numberLottery'])
            queryset = NumberLottery.objects.filter(numberLottery__in=listNumber)
        serializer = self.get_serializer(queryset, many=True)
        self.response["result"] = serializer.data
        return Response(self.response)

class ListNumberLottery(LottAPIGetView):
    
    queryset = NumberLottery.objects.all()
    serializer_class = SlzListNumber
    pagination_class = None
    
    def get(self, request, *args, **kwargs):
        queryset = NumberLottery.objects.all()
        if not self.request.user.account.admin:
            queryset = NumberLottery.objects.filter(user=self.request.user.account)
    
        serializer = self.get_serializer(queryset, many=True)
        self.response["result"] = serializer.data
        return Response(self.response)

def addNumberApi(request):
    numberLottery = request.POST['number']
    account = Account.objects.get(user=request.user)
    number = NumberLottery.objects.filter(numberLottery=numberLottery, user=account)
    if len(numberLottery) != 6:
        return 'หมายเลขนี้ไม่ถูกต้อง', numberLottery, False
    if number.exists():
        return 'หมายเลขนี้มีอยู่แล้ว', numberLottery, False
    checkNumber(numberLottery, account)
    return "", "", True

def checkNumber(numberLottery, account):
    prototype = PrototypeNumberLottery.objects.filter(numberLottery=numberLottery)
    number = NumberLottery.objects.create(numberLottery=numberLottery, user=account)
    if prototype.exists():
        prototype[0].matching.add(number)
    else:
        prototype = PrototypeNumberLottery.objects.create(numberLottery=numberLottery)
        prototype.matching.add(number)

def deleteNumberApi(request):
    form =DeleteNumberLotteryForm(request.POST)
    if not form.is_valid():
        return 'หมายเลขนี้ไม่มีอยู่แล้ว', False
    IDNumberDelete = form['IDNumberDelete'].data
    NumberLottery.objects.filter(pk=IDNumberDelete).delete()
    return form, True

def addDuplicateNumber(request):
    numberLottery = request.POST['numberDuplicate']
    if len(numberLottery) != 6:
        return redirect(reverse('addlotterypage'))
    prototype = PrototypeNumberLottery.objects.filter(numberLottery=numberLottery)
    number = NumberLottery.objects.create(numberLottery=numberLottery, user=request.user.account)
    if prototype.exists():
        prototype[0].matching.add(number)
    else:
        prototype = PrototypeNumberLottery.objects.create(numberLottery=numberLottery)
        prototype.matching.add(number)
    return redirect(reverse('addlotterypage'))