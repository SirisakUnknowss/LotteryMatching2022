#Django
from django.db import models
from django.contrib.auth.models import User
#Project
from shop.models import Shop

# Create your models here.
class NumberLottery(models.Model):
        
    numberLottery   = models.CharField(max_length=6, null=True, blank=True)
    isRead          = models.BooleanField(default=False)
    user            = models.OneToOneField(User, null=True, blank=True, related_name='accountNumberLottery', on_delete=models.CASCADE)