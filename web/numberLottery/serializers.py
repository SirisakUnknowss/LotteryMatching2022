from rest_framework import serializers

from shop.models import Shop
from .models import NumberLottery, PrototypeNumberLottery
from account.serializers import SlzAccount

class SlzListNumber(serializers.ModelSerializer):
    user = SlzAccount()
    class Meta:
        model = NumberLottery
        fields = '__all__'

    def to_representation(self, instance):
        response = super(SlzListNumber, self).to_representation(instance)
        try:
            response["idShop"] = Shop.objects.get(pk=instance.idShop).name
            return response
        except:
            return response

class SlzListNumberMatching(serializers.ModelSerializer):
    # user = SlzAccount()
    matching = SlzListNumber(many=True)
    class Meta:
        model = PrototypeNumberLottery
        fields = '__all__'

class SlzAddNumberInput(serializers.Serializer):
    number = serializers.CharField(required=True, max_length=6)