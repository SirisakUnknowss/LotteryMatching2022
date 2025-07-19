import csv
from django.core.management.base import BaseCommand
from numberLottery.models import PrototypeNumberLottery

class Command(BaseCommand):
    help = "Export PrototypeNumberLottery data to CSV"

    def handle(self, *args, **kwargs):
        with open('prototype_lottery_export.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['numberLottery', 'isRead', 'matching_ids'])

            # ใช้ iterator เพื่อลด memory consumption
            for obj in PrototypeNumberLottery.objects.prefetch_related('matching').iterator():
                matching_ids = ','.join(str(m.id) for m in obj.matching.all())
                writer.writerow([obj.numberLottery, obj.isRead, matching_ids])