from rest_framework import serializers

from .models import Shop

class SlzShop(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'