from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('code', 'name_ar', 'name_en', 'tax_number', 'status','manager')