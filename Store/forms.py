from django import forms
from .models import *


class VerkaufenForm(forms.ModelForm):
    class Meta:
        model = Verkaufen
        fields = ['sort', 'product', ]
        widgets = {
            'sort': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
        }
