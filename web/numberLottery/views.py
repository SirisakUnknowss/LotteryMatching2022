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
from .serializers import SlzListNumber, SlzListNumberMatching

# Create your views here.
class ListNumberLotteryMatching(LottAPIGetView):

    queryset = NumberLottery.objects.all()
    serializer_class = SlzListNumberMatching
    pagination_class = None
    
    def get(self, request, *args, **kwargs):
        prototype = PrototypeNumberLottery.objects.filter(matching__isnull=False).values('id', 'numberLottery').annotate(count=Count('id')).filter(count__gt=1)
        listNumber = []
        queryset = None
        for numberMatching in prototype:
            listNumber.append(numberMatching['numberLottery'])
        queryset = PrototypeNumberLottery.objects.filter(numberLottery__in=listNumber)
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
    # shopSelect = ""
    # if request.user.account.admin:
    shopSelect = request.POST['shopSelect']
    account = Account.objects.get(user=request.user)
    number = NumberLottery.objects.filter(numberLottery=numberLottery, user=account, idShop=shopSelect)
    form = { "errorAddNumber":None, "numberList":None, "idShop":None }
    if len(numberLottery) != 6:
        form["errorAddNumber"] = "หมายเลขนี้ไม่ถูกต้อง"
        form["numberList"] = numberLottery
        form["idShop"] = shopSelect
        return form, False
    if number.exists():
        form["errorAddNumber"] = "หมายเลขนี้มีอยู่แล้ว"
        form["numberList"] = numberLottery
        form["idShop"] = shopSelect
        return form, False
    if not numberLottery.isnumeric():
        form["errorAddNumber"] = "หมายเลขนี้ไม่ถูกต้อง"
        form["numberList"] = numberLottery
        form["idShop"] = shopSelect
        return form, False
    
    checkNumber(numberLottery, shopSelect, account)
    return form, True

def addManyNumberApi(request):
    # shopSelect = ""
    # if request.user.account.admin:
    shopSelect = request.POST['shopSelect']
    numberList = request.POST['numberList']
    print(numberList)
    account = Account.objects.get(user=request.user)
    formData, isSuccess = validateAndAddNumber(account, shopSelect, numberList)
    form = { "errorAddNumber":None, "numberList":None, "idShop":None }
    if isSuccess:
        return form, True
    form["errorAddNumber"] = formData
    return form, False

def validateAndAddNumber(account, shopSelect, numberList):
    listNumberError = []
    numberLists = numberList.split("\n")
    print(numberLists)
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
    form =DeleteNumberLotteryForm(request.POST)
    if not form.is_valid():
        return 'หมายเลขนี้ไม่มีอยู่แล้ว', False
    IDNumberDelete = form['IDNumberDelete'].data
    NumberLottery.objects.filter(pk=IDNumberDelete).delete()
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
    NumberLottery.objects.filter(pk=idNumber).update(isRead=True)
    return redirect(reverse(page))