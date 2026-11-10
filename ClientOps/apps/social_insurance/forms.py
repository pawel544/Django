from django import forms
from .models import InsurancePeriod

class InsurancePeriodForm(forms.ModelForm):
    class Meta:
        model = InsurancePeriod
        fields = ('employee', 'valid_from', 'valid_to', 'registration_date','termination_date', 'status')