# Python

# Django
from django.core.management.base import BaseCommand
# Project
from numberLottery.models import NumberLottery
from shop.models import Shop

class Command(BaseCommand):
    #sudo docker-compose -f docker-compose-prod.yaml exec web sh -c "python manage.py deleteNumberNoShop"
    help = "remove numberLottery not have shop all"

    def handle(self, *args, **options):
        self.removeDataAll()
    
    def removeDataAll(self):
        numberList = NumberLottery.objects.all()
        shopList = Shop.objects.all()
        print("number count before === " + numberList.count())
        for shop in shopList:
            numberList.exclude(idShop=shop.pk)
        print("number count after === " + numberList.count())