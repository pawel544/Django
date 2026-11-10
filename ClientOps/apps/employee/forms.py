from django import forms

from .models import Employee


class EmployeeForm(forms.ModelForm):
    MISSING_INFORMATION_CHOICES = [
        ("national_id", "National ID"),
        ("insurance_number", "Insurance number"),
        ("birth_date", "Birth date"),
        ("hire_date", "Hire date"),
        ('job_title', 'Job title'),
        ("salary", "Salary"),
    ]
    missing_information =forms.MultipleChoiceField(
        choices=MISSING_INFORMATION_CHOICES,
        required=False,
        widget= forms.CheckboxSelectMultiple
        )
    reason= forms.CharField(required=False,widget=forms.Textarea)
    class Meta:
        model = Employee

        fields = [
            "national_id",
            "birth_date",
            "hire_date",
            "insurance_number",
            "job_title",
            "salary",
        ]