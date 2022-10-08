from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from numberLottery.models import NumberLottery, PrototypeNumberLottery

# Register your models here.

class NumberLotteryResource(resources.ModelResource):
    class Meta:
        model = NumberLottery
        import_id_fields = ('numberLottery',)
        exclude = ('id',)


@admin.register(NumberLottery)
class NumberLotteryAdmin(ImportExportModelAdmin):
    resource_class = NumberLotteryResource
    list_display = ['id', 'numberLottery', 'isRead']
    search_fields = ['numberLottery']
    list_filter    = ['numberLottery', 'idShop', 'isRead']

class PrototypeNumberLotteryResource(resources.ModelResource):
    class Meta:
        model = PrototypeNumberLottery
        import_id_fields = ('numberLottery',)
        exclude = ('id',)

@admin.register(PrototypeNumberLottery)
class PrototypeNumberLotteryAdmin(ImportExportModelAdmin):
    resource_class = PrototypeNumberLotteryResource
    list_display = ['id', 'numberLottery']
    search_fields = ['numberLottery']
    list_filter    = ['numberLottery', 'matching__idShop', 'matching__isRead']