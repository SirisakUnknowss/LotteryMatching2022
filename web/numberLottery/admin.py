from import_export import fields, resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from numberLottery.models import NumberLottery, PrototypeNumberLottery

# Register your models here.

class NumberLotteryResource(resources.ModelResource):
    class Meta:
        model = NumberLottery
        import_id_fields = ('numberLottery',)
        exclude = ('id', 'user')


@admin.register(NumberLottery)
class NumberLotteryAdmin(ImportExportModelAdmin):
    resource_class = NumberLotteryResource
    list_display = ['id', 'numberLottery', 'isRead']
    search_fields = ['numberLottery']
    list_filter    = ['idShop', 'isRead']
    list_per_page = 500

class PrototypeNumberLotteryResource(resources.ModelResource):
    matching_ids = fields.Field(column_name='matching_ids')
    class Meta:
        model = PrototypeNumberLottery
        import_id_fields = ('numberLottery',)
        exclude = ('id',)

    def get_queryset(self):
        return super().get_queryset().iterator()

    def dehydrate_matching_ids(self, obj):
        return obj.matching_ids()


@admin.register(PrototypeNumberLottery)
class PrototypeNumberLotteryAdmin(ImportExportModelAdmin):
    resource_class = PrototypeNumberLotteryResource
    list_display = ['id', 'numberLottery']
    search_fields = ['numberLottery']
    list_filter    = ['numberLottery', 'matching__idShop', 'matching__isRead']