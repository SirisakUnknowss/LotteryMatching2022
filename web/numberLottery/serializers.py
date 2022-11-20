from rest_framework import serializers

from shop.models import Shop
from .models import NumberLottery, PrototypeNumberLottery

class SlzListNumber(serializers.ModelSerializer):
    class Meta:
        model = NumberLottery
        fields = ['id', 'numberLottery']

    def to_representation(self, instance):
        response = super(SlzListNumber, self).to_representation(instance)
        response["username"] = instance.username
        try:
            response["idShop"] = Shop.objects.get(pk=instance.idShop).name
            return response
        except:
            return response

class SlzNumberMatching(serializers.ModelSerializer):

    class Meta:
        model = NumberLottery
        fields = []

    def to_representation(self, instance):
        response = super(SlzNumberMatching, self).to_representation(instance)
        response["username"] = instance.username
        try:
            response["idShop"] = Shop.objects.get(pk=instance.idShop).name
            return response
        except:
            return response

class SlzListNumberMatching(serializers.ModelSerializer):
    matching = SlzNumberMatching(many=True)
    class Meta:
        model = PrototypeNumberLottery
        fields = '__all__'

class SlzAddNumberInput(serializers.Serializer):
    number = serializers.CharField(required=True, max_length=6)

class SlzListNumberEachShop(serializers.ModelSerializer):
    class Meta:
        model = NumberLottery
        fields = '__all__'

    def to_representation(self, instance):
        response = super(SlzListNumberEachShop, self).to_representation(instance)
        try:
            response["idShop"] = Shop.objects.get(pk=instance.idShop).name
            return response
        except:
            return response