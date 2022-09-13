#Django
from django import forms
from django.shortcuts import redirect
from django.urls import reverse

class AuthenForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

    def clean(self):
        cleaned_data = super().clean()
        try:
            username = cleaned_data['username']
            password = cleaned_data['password']
            if not username and not password:
                self.add_error('username', "UserName incorrect!")
                self.add_error('password', "Password incorrect!")
            return cleaned_data
        except:
            return redirect(reverse('homepage'))