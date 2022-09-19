from rest_framework import serializers

from .models import Account
from shop.serializers import SlzShop

class SlzAccount(serializers.ModelSerializer):
    shop = SlzShop()
    class Meta:
        model = Account
        fields = '__all__'