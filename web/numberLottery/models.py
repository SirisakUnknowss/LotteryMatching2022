#Django
from django.db import models
#Project
from account.models import Account

# Create your models here.
class NumberLottery(models.Model):
        
    numberLottery   = models.CharField(max_length=6, null=True, blank=True)
    isRead          = models.BooleanField(default=False)
    user            = models.OneToOneField(Account, null=True, blank=True, related_name='accountNumberLottery', on_delete=models.CASCADE)
    
    @staticmethod
    def createNumberRecord(number, user):
        NumberLottery.objects.create(numberLottery=number, user=user)