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
        count = 0
        for number in numberList:
            if not Shop.objects.filter(pk=number.idShop).exists():
                # print(f"number === {number.numberLottery}")
                count += 1
                
        print(numberList.count())
        print(count)

        self.stdout.write(self.style.SUCCESS('Remove All Complete'))
        