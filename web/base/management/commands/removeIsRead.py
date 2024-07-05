# Python

# Django
from django.core.management.base import BaseCommand
# Project
from numberLottery.models import NumberLottery, PrototypeNumberLottery

class Command(BaseCommand):
    #sudo docker-compose -f docker-compose-prod.yaml exec web sh -c "python manage.py removeIsRead --name prototype"
    #sudo docker-compose -f docker-compose-prod.yaml exec web sh -c "python manage.py removeIsRead --name numberLottery"
    help = "remove data by name"

    LIST_DATA = [ 'prototype', 'numberLottery', ]

    def add_arguments(self, parser):
        parser.add_argument(
            '--name',
            help='remove data by name',
        )

    def handle(self, *args, **options):
        self.removeDataAll(options['name'])
    
    def removeDataAll(self, name):
        if not name in Command.LIST_DATA:
            self.stdout.write(self.style.ERROR("{} invalid name".format(name)))
            return
        if name == Command.LIST_DATA[0]:
            PrototypeNumberLottery.objects.all().update(isRead=False)
        elif name == Command.LIST_DATA[1]:
            NumberLottery.objects.all().update(isRead=False)
        self.stdout.write(self.style.SUCCESS('Update {} All Complete').format(name))