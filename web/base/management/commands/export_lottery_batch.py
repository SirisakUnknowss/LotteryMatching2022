import csv
from django.core.management.base import BaseCommand
from numberLottery.models import PrototypeNumberLottery

class Command(BaseCommand):
    help = "Export PrototypeNumberLottery in batches"

    def add_arguments(self, parser):
        parser.add_argument('--batch-size', type=int, default=100000)
        parser.add_argument('--start', type=int, default=0)

    def handle(self, *args, **options):
        batch_size = options['batch_size']
        start = options['start']
        end = start + batch_size

        filename = f'lottery_batch_{start}_{end}.csv'
        queryset = PrototypeNumberLottery.objects.prefetch_related('matching').order_by('id')[start:end]

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['numberLottery', 'isRead', 'matching_ids'])

            for obj in queryset.iterator():
                match_ids = ','.join(str(m.id) for m in obj.matching.all())
                writer.writerow([obj.numberLottery, obj.isRead, match_ids])

        self.stdout.write(self.style.SUCCESS(f'Batch export complete: {filename}'))