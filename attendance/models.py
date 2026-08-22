from django.db import models
from django.utils import timezone

from sites.models import Site


class Employee(models.Model):
    name = models.CharField(max_length=150)
    employee_code = models.CharField(max_length=50, unique=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.employee_code} - {self.name}"


class AttendanceRecord(models.Model):
    class Status(models.TextChoices):
        PRESENT = "present", "Present"
        ABSENT = "absent", "Absent"
        LEAVE = "leave", "Leave"
        HALF_DAY = "half_day", "Half Day"

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.localdate)
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PRESENT)

    class Meta:
        unique_together = ("employee", "date")

    @property
    def working_hours(self):
        if self.check_in and self.check_out:
            return round((self.check_out - self.check_in).total_seconds() / 3600, 2)
        return 0
