from django import forms
from .models import Home


class HomesForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ('city', 'adress', 'home_number', 'home_sub_number')
