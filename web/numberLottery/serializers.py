from rest_framework import serializers

from shop.models import Shop
from .models import NumberLottery, PrototypeNumberLottery

class SlzListNumber(serializers.ModelSerializer):
    idShop      = serializers.SerializerMethodField()
    username    = serializers.CharField(source='user.username', default='-')

    class Meta:
        model = NumberLottery
        fields = '__all__'

    def get_idShop(self, instance):
        shop = Shop.objects.filter(pk=instance.idShop).first()
        return shop.name if shop else None

    def to_representation(self, instance):
        # เรียกตัว parent ก่อน (ได้ dict ทั้งหมด)
        rep = super().to_representation(instance)
        # ตัดเหลือแค่ 2 ฟิลด์ที่ต้องการ
        filtered_rep = {key: rep[key] for key in ['id', 'numberLottery', 'username']}
        return filtered_rep

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