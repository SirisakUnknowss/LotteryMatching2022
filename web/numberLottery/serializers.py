from rest_framework import serializers

from .models import NumberLottery, PrototypeNumberLottery
from account.serializers import SlzAccount

class SlzListNumber(serializers.ModelSerializer):
    user = SlzAccount()
    class Meta:
        model = NumberLottery
        fields = '__all__'

class SlzListNumberMatching(serializers.ModelSerializer):
    # user = SlzAccount()
    class Meta:
        model = PrototypeNumberLottery
        fields = '__all__'

class SlzAddNumberInput(serializers.Serializer):
    number = serializers.CharField(required=True, max_length=6)