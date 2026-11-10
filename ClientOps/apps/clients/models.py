from django.db import models
from django.db.models.base import ModelBase
from django.conf import settings

# Create your models here.

class ServiceType(models.Model):
    ROLE_CHOICES=[("payroll", "Payroll"),
                  ("social_insurance", "Social Insurance"),
                  ("accounting", "Accounting"),
                  ("tax", "Tax"),
                  ("insurance_contracting", "Insurance Contracting")]
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50, choices=ROLE_CHOICES)
    def __str__(self):
        return self.get_name_display()


class Client(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name_ar = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    tax_number = models.CharField(max_length=50, unique=True)
    status =models.CharField(max_length=50)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True,
                   blank=True, related_name="managed_clients")
    service = models.ForeignKey(ServiceType, on_delete=models.CASCADE ,related_name='client_assignments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.code} - {self.name_ar}'

class ClientContact(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='clients')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(blank =True)
    phone = models.CharField(max_length=50)
    job_title = models.CharField(max_length=100, blank=True)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class ClientAssignment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='assignments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
                         related_name='client_assignments')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['client', 'user'],
                name='unique_assignment_client',
            )
        ]
    def __str__(self):
        return f'{self.client} {self.user}'

class ClientService(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='services',)
    service_type = models.ForeignKey(ServiceType, on_delete=models.PROTECT, related_name='service_type' )
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['client', 'service_type'],
                name='unique_service_client',
            )
        ]
        def __str__(self):
            return f"{self.client} - {self.get_service_display()}"
