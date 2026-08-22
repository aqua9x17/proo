from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = "admin", "Admin"
        MANAGER = "manager", "Manager"
        OPERATOR = "operator", "Operator"

    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.OPERATOR)

    def is_admin(self):
        return self.role == self.Roles.ADMIN or self.is_superuser

    def is_manager(self):
        return self.role in {self.Roles.ADMIN, self.Roles.MANAGER} or self.is_superuser
