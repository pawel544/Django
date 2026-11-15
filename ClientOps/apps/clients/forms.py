from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        #fields = '__all__'
        fields = ('code', 'name_ar', 'name_en', 'tax_number', 'status','manager', 'service')
        widgets = {
            'service': forms.Select(
                attrs={'class': 'form-control'}
            )
        }