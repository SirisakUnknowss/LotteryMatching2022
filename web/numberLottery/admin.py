from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from numberLottery.models import NumberLottery

# Register your models here.

class AccountResource(resources.ModelResource):
    class Meta:
        model = NumberLottery
        import_id_fields = ('numberLottery',)


@admin.register(NumberLottery)
class AccountAdmin(ImportExportModelAdmin):

    list_display = ['id', 'numberLottery', 'isRead']