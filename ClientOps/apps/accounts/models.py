from django.contrib.auth.models import  AbstractUser
from django.db import models
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=12345, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email=email, password=password, **extra_fields)



class User(AbstractUser):
    ROLE_CHOICES = [
        ("Admin","Admin"),
        ("Supervisor","Supervisor"),
        ("Employee","Employee")
                    ]
    username = None
    email = models.EmailField(unique=True)
    objects = CustomUserManager()
    first_login=models.BooleanField(default=True)
    number_login = models.IntegerField(default=0)
    blocked_user = models.BooleanField(default=False)
    role = models.CharField(choices=ROLE_CHOICES, max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email

