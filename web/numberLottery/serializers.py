from rest_framework import serializers

from .models import NumberLottery
from account.serializers import SlzAccount

class SlzListNumber(serializers.ModelSerializer):
    user = SlzAccount()
    class Meta:
        model = NumberLottery
        fields = '__all__'

class SlzAddNumberInput(serializers.Serializer):
    number = serializers.CharField(required=True, max_length=6)