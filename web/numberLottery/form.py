#Django
from django import forms
from django.shortcuts import redirect
from django.urls import reverse

class DeleteNumberLotteryForm(forms.Form):
    IDNumberDelete = forms.CharField(max_length=6)

    def clean(self):
        cleaned_data = super().clean()
        try:
            IDNumberDelete = cleaned_data['IDNumberDelete']
            if not IDNumberDelete:
                self.add_error('IDNumberDelete', "incorrect")
            return cleaned_data
        except:
            return redirect(reverse('addlotterypage'))