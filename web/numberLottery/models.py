#Django
from django.db import models
#Project
from account.models import Account

# Create your models here.
class NumberLottery(models.Model):
        
    numberLottery   = models.CharField(max_length=6, null=True, blank=True)
    isRead          = models.BooleanField(default=False)
    idShop          = models.CharField(max_length=9, null=True, blank=True)
    user            = models.ForeignKey(Account, null=True, blank=True, related_name='accountNumberLottery', on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.numberLottery

    @property
    def username(self):
        return str(self.user.username)
    
    @staticmethod
    def createNumberRecord(number, user):
        NumberLottery.objects.create(numberLottery=number, user=user)

class PrototypeNumberLottery(models.Model):
        
    numberLottery   = models.CharField(max_length=6, unique=True)
    matching        = models.ManyToManyField(NumberLottery, blank=True)
    isRead          = models.BooleanField(default=False)
    
    def __str__(self):
        return self.numberLottery

    @staticmethod
    def createNumberRecord(number):
        PrototypeNumberLottery.objects.create(numberLottery=number)