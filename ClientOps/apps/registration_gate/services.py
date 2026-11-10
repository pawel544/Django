from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db import transaction
from .models import RegistrationBlock


@transaction.atomic
def approved_registration(*, registrationblock, employee, reason):
    if registrationblock.employee != employee:
        raise ValidationError("You cannot change the status of this employee.")

    registrationblock.status = RegistrationBlock.Status.APPROVED
    registrationblock.reason = reason.strip()
    registrationblock.reviewed_at=timezone.now()
    registrationblock.save(update_fields=['status', 'reason', 'reviewed_at'])
    return registrationblock

@transaction.atomic
def rejected_registration(*, registrationblock, employee, reason):
    if registrationblock.employee != employee:
        raise ValidationError("You cannot change the status of this employee.")

    registrationblock.status = RegistrationBlock.Status.REJECTED
    registrationblock.reason = reason.strip()
    registrationblock.reviewed_at=timezone.now()
    registrationblock.save(update_fields=['status', 'reason', 'reviewed_at'])
    return registrationblock

@transaction.atomic
def completed_registration(*, registrationblock, employee, reason):
    if registrationblock.employee != employee:
        raise ValidationError("You cannot change the status of this employee.")

    registrationblock.status = RegistrationBlock.Status.COMPLETED
    registrationblock.reason = reason.strip()
    registrationblock.reviewed_at=timezone.now()
    registrationblock.save(update_fields=['status', 'reason', 'reviewed_at'])
    return registrationblock

