from django.db import models

from ClientOps.apps.employee.models import Employee
from ...ClientOps.settings import AUTH_USER_MODEL

# Create your models here.


class RegistrationBlock(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending" , "Pending"
        APPROVED = "approved" , "Approved"
        REJECTED = "rejected" , "Rejected"
        COMPLETED = "completed" , "Completed"

    employee = models.OneToOneField(Employee,on_delete=models.PROTECT,related_name="registration_gate")
    status = models.CharField(choices= Status.choices, max_length= 20, default = Status.PENDING)
    missing_information = models.JSONField(default=list, blank=True)
    reason = models.TextField(null=True, blank=True)
    submitted_at = models.DateTimeField(null=True, blank=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    approved_by = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.PROTECT,null=True,blank=True,
        related_name="approved_registrations")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]