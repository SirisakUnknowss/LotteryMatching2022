from django.shortcuts import render
from rest_framework.response import Response

from base.views import LottListView, LottAPIView
from numberLottery.models import NumberLottery
from numberLottery.serializers import SlzListNumber, SlzAddNumberInput
from account.models import Account

# Create your views here.
class ListNumberLottery(LottListView):
    """
    """
    queryset = NumberLottery.objects.all()
    serializer_class = SlzListNumber
    pagination_class = None
    
class AddNumberLottery(LottAPIView):
    queryset            = NumberLottery.objects.all()
    serializer_class    = SlzListNumber

    def post(self, request, *args, **kwargs):
        serializerInput         = SlzAddNumberInput(data=self.request.data)
        serializerInput.is_valid(raise_exception=True)
        numberInput             = serializerInput.validated_data['numberInput']
        account                 = Account.objects.get(user=self.request.user)
        NumberLottery.createNumberRecord(numberInput, account)
        serializer              = self.get_serializer(account)
        self.response["result"] = serializer.data
        return Response(self.response)