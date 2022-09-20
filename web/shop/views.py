#Project
from .serializers import SlzShop
from .form import AddShopForm
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

class ListShow(LottListView):
    """
    """
    queryset = Shop.objects.all()
    serializer_class = SlzShop
    pagination_class = None