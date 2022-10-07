#Django
from django import forms
from django.shortcuts import redirect
from django.urls import reverse

#Project
from account.models import Account
from .models import Shop

class AddShopForm(forms.Form):
    name = forms.CharField(max_length=50)

    def clean(self):
        cleaned_data = super().clean()
        try:
            name = cleaned_data['name']
            if not name:
                self.add_error('name', "incorrect")
            self.existShop(cleaned_data)
            return cleaned_data
        except:
            return redirect(reverse('shoppage'))

    def existShop(self, cleaned_data):
        try:
            Shop.objects.get(name=cleaned_data['name'])
            self.add_error('name', "exist")
        except Shop.DoesNotExist:
            return

    def existUsername(self, cleaned_data):
        try:
            inputUsername = cleaned_data['inputUsername']
            if not inputUsername:
                self.add_error('inputUsername', "incorrect")
            Account.objects.get(username=cleaned_data['inputUsername'])
            self.add_error('inputUsername', "usernameExist")
        except Shop.DoesNotExist:
            return

class DeleteShopForm(forms.Form):
    IDShopDelete = forms.CharField(max_length=50)

    def clean(self):
        cleaned_data = super().clean()
        try:
            IDShopDelete = cleaned_data['IDShopDelete']
            if not IDShopDelete:
                self.add_error('IDShopDelete', "incorrect")
            return cleaned_data
        except:
            return redirect(reverse('shoppage'))