from django.contrib.auth.models import User
from django.db import models
from ..clients.models import Client
from ...ClientOps.settings import AUTH_USER_MODEL
# Create your models here.

class Employee(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        TERMINATED = "terminated", "Terminated"
        ON_LEAVE = "on_leave", "On Leave"
        RELEASED = "released", "Released"
    client =models.ForeignKey(Client, on_delete=models.PROTECT, null=True, blank=True ,related_name='employees')
    national_id = models.CharField(max_length = 120)
    employee = models.OneToOneField(User ,on_delete=models.PROTECT,related_name='employee_profile', null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    birth_date = models.DateField(null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    termination_date = models.DateField(null=True, blank=True)
    insurance_number = models.CharField(max_length=120,null=True, blank=True)
    job_title = models.CharField(max_length=120, null=True, blank=True)
    salary =models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)

class EmployeeHistory(models.Model):
    employee_record =models.ForeignKey(Employee, on_delete=models.PROTECT,
                                       related_name='history')
    client = models.ForeignKey(Client ,on_delete=models.PROTECT,null=True,
                               blank=True, related_name='client_history')
    user = models.ForeignKey(AUTH_USER_MODEL ,on_delete=models.PROTECT, related_name='Employee_history')

    termination_date = models.DateField(null=True, blank=True)
    insurance_number = models.CharField(max_length=120,)
    job_title = models.CharField(max_length=120,)
    salary =models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=Employee.Status.choices,)
    recorded_at = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()
    class Meta:
        ordering = ['-recorded_at']

    def __str__(self):
        return f"History for employee #{self.employee_record_id} at {self.recorded_at}"
