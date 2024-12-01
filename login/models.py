from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    type = models.CharField(max_length=20, choices=[
        ("business","Business"),
        ("customer","Customer")
    ])
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.type} account of {self.user.username}"
   