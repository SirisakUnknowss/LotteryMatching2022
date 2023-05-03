# Python

# Django
from django.core.management.base import BaseCommand, CommandError
# Project
from numberLottery.models import NumberLottery
from shop.models import Shop

class Command(BaseCommand):
    #sudo docker-compose -f docker-compose-prod.yaml exec web sh -c "python manage.py deleteData --name shop"
    #sudo docker-compose -f docker-compose-prod.yaml exec web sh -c "python manage.py deleteData --name numberLottery"
    help = "delete data by name"

    LIST_DATA = [
                        'shop',
                        'numberLottery',
                    ]

    def add_arguments(self, parser):
        parser.add_argument(
            '--name',
            help='delete data by name',
        )

    def handle(self, *args, **options):
        self.deleteDataAll(options['name'])
    
    def deleteDataAll(self, name):
        
        if not name in Command.LIST_DATA:
            self.stdout.write(self.style.ERROR("{} invalid name".format(name)))
            return
        if name == Command.LIST_DATA[0]:
            Shop.objects.all().delete()
        elif name == Command.LIST_DATA[1]:
            NumberLottery.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Delete {} All Complete').format(name))