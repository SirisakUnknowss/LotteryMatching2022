from rest_framework import serializers

from .models import Shop
from account.models import Account

class SlzAccount(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class SlzShop(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'

    def to_representation(self, instance):
        response = super(SlzShop, self).to_representation(instance)
        accounts = Account.objects.filter(shop=instance.pk)
        response["account"] = SlzAccount(accounts, many=True).data
        return response