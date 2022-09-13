from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from account.models import Account

# Register your models here.

class AccountResource(resources.ModelResource):
    class Meta:
        model = Account
        import_id_fields = ('username',)


@admin.register(Account)
class AccountAdmin(ImportExportModelAdmin):

    list_display = ['id', 'username', 'password', 'admin']