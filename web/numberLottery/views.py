#Project
from base.views import LottListView
from account.models import Account
from .models import NumberLottery
from .form import AddNumberLotteryForm
from .serializers import SlzListNumber

# Create your views here.
class ListNumberLottery(LottListView):
    """
    """
    queryset = NumberLottery.objects.all()
    serializer_class = SlzListNumber
    pagination_class = None
    
def addNumberApi(request):
    form = AddNumberLotteryForm(request.POST)
    if not form.is_valid():
        if 'exist' in str(form):
            return 'หมายเลขนี้มีอยู่แล้ว', False
        if 'incorrect' in str(form):
            return 'หมายเลขนี้ไม่ถูกต้อง', False
        return 'กรุณากรอกข้อมูลใหม่อีกครั้ง', False
    numberLottery = form['number'].data
    account = Account.objects.get(user=request.user)
    NumberLottery.objects.create(numberLottery=numberLottery, user=account)
    return form, True