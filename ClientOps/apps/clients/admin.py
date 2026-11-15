from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Client)
admin.site.register(models.ClientContact)
admin.site.register(models.ClientAssignment)
admin.site.register(models.ClientService)