#Django
from django import forms
from django.shortcuts import redirect
from django.urls import reverse

#Project
from .models import NumberLottery

class AddNumberLotteryForm(forms.Form):
    number = forms.CharField(max_length=6)

    def clean(self):
        cleaned_data = super().clean()
        try:
            number = cleaned_data['number']
            if not number:
                self.add_error('number', "incorrect")
            self.existNumber(cleaned_data)
            return cleaned_data
        except:
            return redirect(reverse('addlotterypage'))

    def existNumber(self, cleaned_data):
        try:
            NumberLottery.objects.get(numberLottery=cleaned_data['number'])
            self.add_error('number', "exist")
        except NumberLottery.DoesNotExist:
            return