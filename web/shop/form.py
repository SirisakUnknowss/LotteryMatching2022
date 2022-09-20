#Django
from django import forms
from django.shortcuts import redirect
from django.urls import reverse

#Project
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
            return redirect(reverse('homepage'))

    def existShop(self, cleaned_data):
        try:
            Shop.objects.get(name=cleaned_data['name'])
            self.add_error('name', "exist")
        except Shop.DoesNotExist:
            return