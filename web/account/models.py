# Module
import secrets, string, six
#Django
from django.db import models
from django.contrib.auth.models import User
#Project
from shop.models import Shop

# Create your models here.
class Account(models.Model):
    name        = models.CharField(max_length=50, null=True, blank=True)
    username    = models.CharField(max_length=50, unique=True)
    password    = models.CharField(max_length=50, null=True, blank=True)
    shop        = models.ForeignKey(Shop, null=True, blank=True, related_name="shopUser", on_delete=models.SET_NULL)
    admin       = models.BooleanField(default=False)
    user        = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='account')

    def __str__(self):
        return self.username

    @staticmethod
    def genUsername():
        """
        Auto generated username for account registration
        """
        num = str(Account.objects.all().count())
        if len(num) > 2:
            num = num[:2]
        else:
            num = "0{}".format(num)
        random = ''.join(secrets.choice(string.digits) for i in range(4)) 
        return "user{}{}".format(num, random)

    @staticmethod
    def createUser():
        username    = Account.genUsername()
        password    = User.objects.make_random_password()
        user        = User.objects.create_user(username=username, email=None, password=password)
        return user