from django.db import models

from ClientOps.apps.employee.models import Employee


# Create your models here.
class InsurancePeriod(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        ACTIVE = "active", "Active"
        TERMINATED = "terminated", "Terminated"
    employee=models.OneToOneField(Employee, related_name='insurance_period', on_delete=models.PROTECT)
    valid_from= models.DateField()
    valid_to= models.DateField(null=True, blank=True)
    registration_date = models.DateField()
    termination_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices , default= Status.PENDING,)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-valid_from"]