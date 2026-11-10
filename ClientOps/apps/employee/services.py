from django.core.exceptions import ValidationError
from django.db import transaction
from ClientOps.apps.employee.models import Employee, EmployeeHistory

@transaction.atomic
def update_employee_salary(*, employee, user, new_salary, reason=""):

    if new_salary <= 0:
        raise ValidationError("Salary must be greater than zero.")
    if new_salary == employee.salary:
        raise ValidationError("The salary cannot be the same as the previous one.")

    EmployeeHistory.objects.create(employee_record=employee,
                                   client =employee.client,
                                   user =user,
                                   termination_date=employee.termination_date,
                                   insurance_number= employee.insurance_number,
                                   job_title=employee.job_title,
                                   salary=employee.salary,
                                   status =  employee.status,
                                   reason = reason
                                   )
    employee.salary = new_salary
    employee.save(update_fields=['salary','updated_at'])
    return employee

@transaction.atomic
def update_employee_job_title(*, employee, user, new_job_title, reason=""):
    new_job_title = new_job_title.strip()
    if not new_job_title:
        raise ValidationError("Job title can't be empty.")
    if new_job_title == employee.job_title:
        raise ValidationError("The job title cannot be the same as the previous one.")
    EmployeeHistory.objects.create(employee_record=employee,
                                   client=employee.client,
                                   user = user,
                                   termination_date=employee.termination_date,
                                   insurance_number=employee.insurance_number,
                                   job_title=employee.job_title,
                                   salary=employee.salary,
                                   status=employee.status,
                                   reason=reason
                                   )
    employee.job_title = new_job_title
    employee.save(update_fields=['job_title','updated_at'])
    return employee

@transaction.atomic
def update_employee_status(*, employee, user, new_status, reason=""):
    if new_status not in Employee.Status.values:
        raise ValidationError("Invalid employee status.")
    if new_status == employee.status:
        raise ValidationError(
            "The status cannot be the same as the previous one.")

    EmployeeHistory.objects.create(employee_record=employee,
                                   client=employee.client,
                                   user = user,
                                   termination_date=employee.termination_date,
                                   insurance_number=employee.insurance_number,
                                   job_title=employee.job_title,
                                   salary=employee.salary,
                                   status=employee.status,
                                   reason=reason
                                   )
    employee.status = new_status
    employee.save(update_fields=['status', 'updated_at'])
    return employee

@transaction.atomic
def update_employee_insurance_number(*, employee, user, new_insurance_number, reason=""):
    if not new_insurance_number not in Employee.insurance_number.strip():
        raise ValidationError("Invalid employee status.")
    if new_insurance_number == employee.insurance_number:
        raise ValidationError(
            "The status cannot be the same as the previous one.")

    EmployeeHistory.objects.create(employee_record=employee,
                                   client=employee.client,
                                   user= user,
                                   termination_date=employee.termination_date,
                                   insurance_number=employee.insurance_number,
                                   job_title=employee.job_title,
                                   salary=employee.salary,
                                   status=employee.status,
                                   reason=reason
                                   )
    employee.insurance_number = new_insurance_number
    employee.save(update_fields=['insurance_number', 'updated_at'])
    return employee

@transaction.atomic
def update_employee_termination_date(*, employee, user, termination_date, reason=""):


    EmployeeHistory.objects.create(employee_record=employee,
                                   client=employee.client,
                                   user= user,
                                   termination_date=employee.termination_date,
                                   insurance_number=employee.insurance_number,
                                   job_title=employee.job_title,
                                   salary=employee.salary,
                                   status=employee.status,
                                   reason=reason
                                   )
    employee.status= Employee.Status.RELEASED
    employee.termination_date = termination_date
    employee.save(update_fields=['termination_date','status' ,'updated_at'])
    return employee