from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import InsurancePeriod
from django.db import transaction

@transaction.atomic
def active_insurance(insurance,user):
    if insurance.status == InsurancePeriod.Status.ACTIVE:
        raise ValidationError("This insurance has already been active")
    if insurance.employee.employee_id != user.pk:
        raise ValidationError("This insurance does not belong to this employee.")
    insurance.insurance_status = InsurancePeriod.Status.ACTIVE
    insurance.updated_at = timezone.now()
    insurance.save( update_fields=["updated_at","insurance_status",] )
    return insurance

@transaction.atomic
def terminated_insurance(insurance,user):
    if insurance.status == InsurancePeriod.Status.TERMINATED:
        raise ValidationError("This insurance has already been terminated")
    if insurance.employee.employee != user.pk:
        raise ValidationError("This insurance does not belong to this employee.")
    insurance.insurance_status = InsurancePeriod.Status.TERMINATED
    insurance.updated_at = timezone.now()
    insurance.save( update_fields=["updated_at","insurance_status",] )
    return insurance

@transaction.atomic
def pending_insurance(insurance,user):
    if insurance.status == InsurancePeriod.Status.PENDING:
        raise ValidationError("This insurance has already been pending")
    if insurance.employee.employee != user.pk:
        raise ValidationError("This insurance does not belong to this employee.")
    insurance.insurance_status = InsurancePeriod.Status.PENDING
    insurance.updated_at = timezone.now()
    insurance.save( update_fields=["updated_at","insurance_status",] )
    return insurance