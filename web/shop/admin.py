from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from shop.models import Shop

# Register your models here.
class AccountResource(resources.ModelResource):
    class Meta:
        model = Shop
        import_id_fields = ('name',)


@admin.register(Shop)
class AccountAdmin(ImportExportModelAdmin):

    list_display = ['id', 'name']
