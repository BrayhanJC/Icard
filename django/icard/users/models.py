import email
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    email = models.EmailField(verbose_name="email address", unique=True, max_length=244)

    # email = models.EmailField(verbose_name="email address", unique=True, max_length=244)
