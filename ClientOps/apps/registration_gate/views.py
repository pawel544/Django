from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from ..employee.forms import EmployeeForm
from ..employee.models import Employee
from models import RegistrationBlock

# Create your views here.


def create_emloyy(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            with transaction.atomic():
                employee = form.save()
                RegistrationBlock.objects.create(employee=employee,
                                  status= RegistrationBlock.Status.PENDING,
                                  missing_information= form.cleaned_data['missing_information'],
                                    reason= form.cleaned_data['reason'],)
                return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, "registration_gate/employee.html",
        {"form": form}
    )

def search_block_employee(request):
    employee = request.GET.get('employee')
    status = request.GET.get('status')
    missing_information = request.GET.get('missing_information')
    submitted_at = request.GET.get('submitted_at')
    reviewed_at = request.GET.get('reviewed_at')
    created_at = request.GET.get('created_at')
    updated_at = request.GET.get('updated_at')
    base= RegistrationBlock.objects.select_related("employee",
        "employee__employee")
    employe = base.all()
    if employee:
        employe= base.filter(employee__employee__icontains=employee)
    if status:
        employe = base.filter(status__icontains=status)
    if missing_information:
        employe =  base.filter(missing_information__icontains=[missing_information])
    if submitted_at:
        employe = base.filter(submitted_at__date=submitted_at)
    if reviewed_at:
        employe = base.filter(reviewed_at__date=reviewed_at)
    if created_at:
        employe = base.filter(created_at__date=created_at)
    if updated_at:
        employe = base.filter(updated_at__date=updated_at)


    return render(request, "registration_gate/employee.html", {"employee": employe})


def cheng_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, isinstance=employee)
        if form.is_valid():
            with transaction.atomic():
                form.save()
                return redirect('employee_list')
        else:
            form = EmployeeForm(isinstance=employee)
    return render(request, "registration_gate/employee.html", {"form": form})

def show_all_block_employees(request):
    employees = RegistrationBlock.objects.all()
    return render(request, "registration_gate/employee.html", {'employees': employees})