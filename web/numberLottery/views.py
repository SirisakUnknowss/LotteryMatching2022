#Django
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.csrf import csrf_exempt
#Project
from base.views import LottAPIGetView, LottListView
from account.models import Account
from shop.models import Shop
from numberLottery.models import NumberLottery, PrototypeNumberLottery
from numberLottery.form import DeleteNumberLotteryForm
from numberLottery.serializers import SlzListNumber, SlzListNumberMatching, SlzListNumberEachShop
from numberLottery.paginations import (
    FiftyPerPagination, TwentyPerPagination, TenPerPagination, SixPerPagePagination
)

# Create your views here.
class ListNumberLotteryMatching(LottListView):
    serializer_class = SlzListNumberMatching
    permission_classes = [ AllowAny ]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    pagination_class = SixPerPagePagination
    
    def get_queryset(self):
        prototype = PrototypeNumberLottery.objects.filter(matching__isnull=False, isRead=False)
        prototype = prototype.values('id', 'numberLottery')
        prototype = prototype.annotate(count=Count('id')).filter(count__gt=1)
        listNumber = []
        queryset = None
        for numberMatching in prototype:
            listNumber.append(numberMatching['numberLottery'])
        queryset = PrototypeNumberLottery.objects.filter(numberLottery__in=listNumber)
        return queryset

class ListNumberLotteryMatchingPagination(LottListView):
    serializer_class    = SlzListNumberMatching
    permission_classes  = [ AllowAny ]
    filter_backends     = [DjangoFilterBackend, filters.OrderingFilter]
    pagination_class    = TenPerPagination
    
    def get_queryset(self):
        prototype = PrototypeNumberLottery.objects.filter(matching__isnull=False, isRead=False)
        prototype = prototype.values('id', 'numberLottery')
        prototype = prototype.annotate(count=Count('id')).filter(count__gt=1)
        listNumber = []
        queryset = None
        for numberMatching in prototype:
            listNumber.append(numberMatching['numberLottery'])
        queryset = PrototypeNumberLottery.objects.filter(numberLottery__in=listNumber)
        # serializer = self.get_serializer(queryset, many=True)
        # self.response["result"] = serializer.data
        return queryset

# Create your views here.
class ListNumberLotteryMatchingRead(LottListView):
    serializer_class = SlzListNumberMatching
    permission_classes = [ AllowAny ]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    pagination_class = SixPerPagePagination
    
    def get_queryset(self):
        prototype = PrototypeNumberLottery.objects.filter(matching__isnull=False, isRead=True)
        prototype = prototype.values('id', 'numberLottery')
        prototype = prototype.annotate(count=Count('id')).filter(count__gt=1)
        listNumber = []
        queryset = None
        for numberMatching in prototype:
            listNumber.append(numberMatching['numberLottery'])
        queryset = PrototypeNumberLottery.objects.filter(numberLottery__in=listNumber)
        return queryset

class ListNumberLottery(LottListView):
    serializer_class = SlzListNumber
    permission_classes = [ AllowAny ]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    pagination_class = SixPerPagePagination
    
    def get_queryset(self):
        shop = self.request.GET.get('shop', None)
        queryset = NumberLottery.objects.filter(idShop=shop).order_by('-id')
        if not self.request.user.account.admin:
            queryset = NumberLottery.objects.filter(user=self.request.user.account,idShop=shop).order_by('-id')
        return queryset

def addNumberApi(request):
    numberLottery = request.POST['number']
    shopSelect = request.POST['shopSelect']
    account = Account.objects.get(user=request.user)
    number = NumberLottery.objects.filter(numberLottery=numberLottery, user=account, idShop=shopSelect)
    form = { "errorAddNumber":None, "numberList":None, "idShop":shopSelect}
    if len(numberLottery) != 6:
        form["errorAddNumber"] = "หมายเลขนี้ไม่ถูกต้อง1"
        form["numberList"] = numberLottery
        return form, False
    if number.exists():
        form["errorAddNumber"] = "หมายเลขนี้มีอยู่แล้ว"
        form["numberList"] = numberLottery
        return form, False
    if not numberLottery.isnumeric():
        form["errorAddNumber"] = "หมายเลขนี้ไม่ถูกต้อง2"
        form["numberList"] = numberLottery
        return form, False
    
    checkNumber(numberLottery, shopSelect, account)
    return form, True

def addManyNumberApi(request):
    shopSelect = request.POST['shopSelect']
    numberList = request.POST['numberList']
    account = Account.objects.get(user=request.user)
    formData, isSuccess = validateAndAddNumber(account, shopSelect, numberList)
    form = { "errorAddNumber":None, "numberList":None, "idShop":shopSelect }
    if isSuccess:
        return form, True
    form["errorAddNumber"] = formData
    return form, False

def validateAndAddNumber(account, shopSelect, numberList):
    listNumberError = []
    numberLists = numberList.split("\n")
    for number in numberLists:
        number = number.replace("\r", "")
        if len(number) < 6:
            continue
        if len(number) > 6:
            numbers = number.split("-")
            number = getNumberScan(numbers)
        if number == None:
            continue
        if len(number) == 6 and number.isnumeric():
            try:
                checkNumber(number, shopSelect, account)
            except:
                listNumberError.append(number)
    if listNumberError.count == 0:
         return "", True
    return listNumberError, False

def getNumberScan(numbers:list):
    for number in numbers:
        if len(number) == 6:
            return number

def checkNumber(numberLottery, shopSelect, account):
    prototype = PrototypeNumberLottery.objects.filter(numberLottery=numberLottery)
    number = NumberLottery.objects.create(numberLottery=numberLottery, user=account, idShop=shopSelect)
    if prototype.exists():
        prototype[0].matching.add(number)
    else:
        prototype = PrototypeNumberLottery.objects.create(numberLottery=numberLottery)
        prototype.matching.add(number)

def deleteNumberApi(request):
    form = DeleteNumberLotteryForm(request.POST)
    if not form.is_valid():
        return 'หมายเลขนี้ไม่มีอยู่แล้ว', False
    IDNumberDelete = form['IDNumberDelete'].data
    NumberLottery.objects.filter(pk=IDNumberDelete).delete()
    shopSelect = request.POST['shopSelect']
    form = { "errorAddNumber":None, "numberList":None, "idShop":shopSelect }
    return form, True

def addDuplicateNumber(request):
    numberLottery = request.POST['numberDuplicate']
    shopSelect = request.POST['shopSelect']
    if len(numberLottery) != 6:
        return redirect(reverse('addlotterypage'))
    prototype = PrototypeNumberLottery.objects.filter(numberLottery=numberLottery)
    number = NumberLottery.objects.create(numberLottery=numberLottery, user=request.user.account, idShop=shopSelect)
    if prototype.exists():
        prototype[0].matching.add(number)
    else:
        prototype = PrototypeNumberLottery.objects.create(numberLottery=numberLottery)
        prototype.matching.add(number)
    return redirect(reverse('addlotterypage'))

def readNumberLottery(request):
    idNumber = request.POST['idNumber']
    page = request.POST['page']
    print(f"page  == {page}")
    try:
        matching = PrototypeNumberLottery.objects.get(pk=idNumber)
        if matching.isRead:
            matching.isRead = False
        else:
            matching.isRead = True
        matching.save()
        return ""
    except PrototypeNumberLottery.DoesNotExist:
        return ""

class ReadNumberLottery(LottAPIGetView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    queryset = PrototypeNumberLottery.objects.all()
    serializer_class = SlzListNumberMatching
    permission_classes = [ AllowAny ]
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        idNumber = self.request.data.get("idNumber")
        print(f"idNumber == {idNumber}")
        try:
            matching = PrototypeNumberLottery.objects.get(pk=idNumber)
            if matching.isRead:
                matching.isRead = False
            else:
                matching.isRead = True
            matching.save()
            self.response["result"] = self.get_serializer(matching).data
            return Response(self.response)
        except PrototypeNumberLottery.DoesNotExist as ex:
            self.response["error"] = str(ex)
            return Response(self.response)

class ListMatchingEachShop(LottAPIGetView):

    queryset = NumberLottery.objects.all()
    serializer_class = SlzListNumberEachShop
    permission_classes = [ AllowAny ]
    
    def get(self, request, *args, **kwargs):
        prototype = PrototypeNumberLottery.objects.filter(matching__isnull=False).values('id', 'numberLottery').annotate(count=Count('id')).filter(count__gt=1)
        listNumber = []
        queryset = None
        for numberMatching in prototype:
            listNumber.append(numberMatching['numberLottery'])
        queryset = NumberLottery.objects.filter(numberLottery__in=listNumber).values('id', 'numberLottery', 'idShop').order_by('idShop')
        self.response["result"] = self.groupNumberByShop(queryset)
        return Response(self.response)
    
    def groupNumberByShop(self, querysets):
        group = {}
        l = []
        shops = Shop.objects.all()
        for shop in shops:
            group[f"{shop.pk}"] = []
        for queryset in querysets:
            if not queryset['numberLottery'] in group[queryset['idShop']]:
                group[queryset['idShop']].append(queryset['numberLottery'])
        for shop in shops:
            data = {}
            if group[f"{shop.pk}"]:
                data['name'] = shop.name
                data['number'] = group[f"{shop.pk}"]
                l.append(data)
        return l
            