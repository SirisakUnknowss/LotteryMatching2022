#Django
from django.db import models
from django.contrib.auth.models import User
#Project
from shop.models import Shop

# Create your models here.
class Account(models.Model):
        
    username    = models.CharField(max_length=50, null=True, blank=True)
    password    = models.CharField(max_length=50, null=True, blank=True)
    shop        = models.ForeignKey(Shop, null=True, blank=True, related_name="shopUser", on_delete=models.SET_NULL)
    admin       = models.BooleanField(default=False)
    user        = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='account')

    def __str__(self):
        return self.name