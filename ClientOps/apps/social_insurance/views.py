from django.shortcuts import render, redirect, get_object_or_404
from ClientOps.apps.social_insurance.forms import InsurancePeriodForm
from ClientOps.apps.social_insurance.models import InsurancePeriod
from django.utils import timezone

from django import forms
# Create your views here.

def all_insurance(request):
    insurance_periods = InsurancePeriod.objects.all()
    return render(request, 'insurance_list.html', {'insurance_periods': insurance_periods})

def insurance_create(request):
    if request.method == 'POST':
        form = InsurancePeriodForm(request.POST)
        if form.is_valid():

            period = form.save(commit=False)
            period.registration_date= timezone.now()
            period.valid_from = timezone.now()
            period.save()
            return redirect('insurance_list')
    else:
        form = InsurancePeriodForm()

        return render(request, 'insurance_create.html', {'form': form})

def search_insurance(request):
    insurance_to = request.GET.get('insurance').strip()
    insurance_periods = InsurancePeriod.objects.select_related("employee").all()
    if insurance_to:

        client = insurance_periods.filter(employee__insurance_number__icontains=insurance_to)
        return render(request, 'insurance_list.html', {'insurance_periods': client})
    return render(request, 'insurance_list.html')

def change_registration_date(request, employee):
    insurance= get_object_or_404(InsurancePeriod, employee=employee)
    if request.method == 'POST':
        data_value= request.POST.get('registration_date')
        if not data_value:
            return render(
                request,
                "change_registration_date.html",
                {
                    "insurance": insurance,
                    "error": "Registration date is required.",
                },
            )
        try:
            registration_date = forms.DateField().clean(data_value)
        except forms.ValidationError:
            return render(
                request,
                "change_registration_date.html",
                {
                    "insurance": insurance,
                    "error": "Enter a valid date.",
                },
            )
        insurance.registration_date = registration_date
        insurance.save(update_fields=['registration_date'])
        return redirect('insurance_list')
    return render(request, 'insurance_list.html', {'insurance': insurance})

def change_termination_date(request, employee):
    insurance = get_object_or_404(InsurancePeriod, employee=employee)
    if request.method == 'POST':
        data_value= request.POST.get('termination_date')
        if not data_value:
            return render(request,
                "change_registration_date.html",
                {
                    "insurance": insurance,
                    "error": "Registration date is required.",
                },
            )
        try:
                termination_date = forms.DateField().clean(data_value)
        except forms.ValidationError:
            return render(request,"change_registration_date.html",
                {
                    "insurance": insurance,
                    "error": "Enter a valid date.",
                },
            )
        insurance.termination_date = termination_date
        insurance.save(update_fields=['termination_date'])
        return redirect('insurance_list')
    return render(request, 'insurance_list.html', {'insurance': insurance,
                                                   "error": "Valid-from date is required."})

def change_valid_from(request, employee):
    insurance= get_object_or_404(InsurancePeriod, employee=employee)
    if request.method == 'POST':
        data_value= request.POST.get('valid_from')
        if not data_value:
            return render(request,"change_registration_date.html",
                {
                    "insurance": insurance,
                    "error": "Enter a valid date"},)
        try:
            valid_from = forms.DateField().clean(data_value)
        except forms.ValidationError:
            return render(request,"change_registration_date.html",
                          {"error": "Enter a valid date."},)
        insurance.valid_from = valid_from
        insurance.save(update_fields=['valid_from'])
        return redirect('insurance_list')
    return render(request, 'insurance_list.html', {'insurance': insurance, })


def change_valid_to(request, employee):
    insurance = get_object_or_404(InsurancePeriod, employee=employee)
    if request.method == 'POST':
        data_value = request.POST.get('valid_to')
        if not data_value:
            return render(request,"change_registration_date.html",
                          {
                              "insurance": insurance,
                              "error": "Enter a valid date"
                          })
        try:
            valid_to = forms.DateField().clean(data_value)
        except forms.ValidationError:
            return render(request,"change_registration_date.html",)
        insurance.valid_to = valid_to
        insurance.save(update_fields=['valid_to'])
        return redirect('insurance_list')
    return render(request, 'insurance_list.html', {'insurance': insurance, })