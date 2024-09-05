# Python
import json
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
        with open('missing_shops.json', 'w') as file:
            missing_shops = []
            for number in numberList:
                if not Shop.objects.filter(pk=number.idShop).exists():
                    number.delete()
                    missing_shops.append({
                        'number_id': number.pk,
                        'isRead': number.isRead,
                        'idShop': number.idShop,
                        'user': number.user.pk,
                    })

            json.dump(missing_shops, file, indent=4)
                
        print(numberList.count())
        print(count)

        self.stdout.write(self.style.SUCCESS('Remove All Complete'))
        