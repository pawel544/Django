from django.contrib.auth.models import  AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ("Admin","Admin"),
        ("Supervisor","Supervisor"),
        ("Employee","Employee")
                    ]
    username = None
    email = models.EmailField(unique=True)

    first_login=models.BooleanField(default=True)
    number_login = models.IntegerField(default=0)
    blocked_user = models.BooleanField(default=False)
    role = models.CharField(choices=ROLE_CHOICES, max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email

