#Django
from collections import defaultdict
from django.shortcuts import redirect
from django.urls import reverse
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import filters
#Project
from base.views import LottAPIGetView, LottListView
from account.models import Account
from shop.models import Shop
from numberLottery.models import NumberLottery, PrototypeNumberLottery
from numberLottery.filter import NumberListFilter, NumberMatchingListFilter
from numberLottery.form import DeleteNumberLotteryForm
from numberLottery.serializers import SlzListNumber, SlzListNumberMatching
from numberLottery.paginations import (FiftyPerPagination, TwentyPerPagination)

class ListNumberLotteryMatching(LottListView):
    serializer_class    = SlzListNumberMatching
    permission_classes  = [ AllowAny ]
    filter_backends     = [DjangoFilterBackend, filters.OrderingFilter]
    pagination_class    = TwentyPerPagination
    filter_class        = NumberMatchingListFilter

    def get_queryset(self):
        return (
            PrototypeNumberLottery.objects
            .filter(isRead=False, matching__isnull=False)
            .annotate(match_count=Count('matching'))
            .filter(match_count__gt=1)  # มีคนกรอกซ้ำมากกว่า 1 คน
            .prefetch_related('matching')  # preload matching เพื่อไม่ query ซ้ำตอน serialize
        )

class ListNumberLotteryMatchingPagination(LottListView):
    serializer_class    = SlzListNumberMatching
    permission_classes  = [ AllowAny ]
    filter_backends     = [DjangoFilterBackend, filters.OrderingFilter]
    pagination_class    = TwentyPerPagination
    filter_class        = NumberMatchingListFilter
    
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

# Create your views here.
class ListNumberLotteryMatchingRead(LottListView):
    serializer_class    = SlzListNumberMatching
    permission_classes  = [ AllowAny ]
    filter_backends     = [DjangoFilterBackend, filters.OrderingFilter]
    pagination_class    = TwentyPerPagination
    filter_class        = NumberMatchingListFilter
    
    def get_queryset(self):
        duplicate_numbers = PrototypeNumberLottery.objects.filter(matching__isnull=False, isRead=True) \
            .values('numberLottery').annotate(count=Count('numberLottery')).filter(count__gt=1) \
            .values_list('numberLottery', flat=True)

        queryset = PrototypeNumberLottery.objects.filter(numberLottery__in=duplicate_numbers)

        return queryset

class ListNumberLottery(LottListView):
    queryset            = NumberLottery.objects.all()
    serializer_class    = SlzListNumber
    permission_classes  = [ AllowAny ]
    filter_backends     = [DjangoFilterBackend, filters.OrderingFilter]
    pagination_class    = TwentyPerPagination
    filter_class        = NumberListFilter
    ordering_fields     = [ 'id' ]
    ordering            = [ '-id' ]

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
    
    IDNumberDelete = request.POST['IDNumberDelete']
    shopSelect = request.POST['shopSelect']
    form = DeleteNumberLotteryForm(request.POST)
    if not form.is_valid():
        form = { "errorAddNumber":form.errors.as_json(), "numberList":IDNumberDelete, "idShop":shopSelect }
        return form, False
    IDNumberDelete = form['IDNumberDelete'].data
    NumberLottery.objects.filter(pk=IDNumberDelete).delete()
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

class ReadNumberLottery(LottAPIGetView):
    queryset            = PrototypeNumberLottery.objects.all()
    serializer_class    = SlzListNumberMatching
    permission_classes  = [ AllowAny ]
    
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        idNumber = self.request.data.get("idNumber")
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
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        duplicate_numbers = (
            PrototypeNumberLottery.objects.filter(matching__isnull=False).values('numberLottery')
            .annotate(num=Count('id')).filter(num__gt=1).values_list('numberLottery', flat=True))
        numberlottery_qs = (NumberLottery.objects.filter(numberLottery__in=duplicate_numbers).select_related(None)
            .values('idShop', 'numberLottery'))
        shop_number_map = defaultdict(set)
        for row in numberlottery_qs:
            shop_number_map[row['idShop']].add(row['numberLottery'])
        shops = Shop.objects.filter(pk__in=shop_number_map.keys())
        shop_name_map = {str(shop.pk): shop.name for shop in shops}
        result = [
            {'name': shop_name_map[str(shop_id)], 'number': list(numbers)}
            for shop_id, numbers in shop_number_map.items()
        ]
        return Response({'result': result})