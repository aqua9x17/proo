from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from sites.models import Site


class Motor(models.Model):
    class Status(models.TextChoices):
        STOPPED = "stopped", "Stopped"
        RUNNING = "running", "Running"
        MAINTENANCE = "maintenance", "Maintenance"

    name = models.CharField(max_length=100)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.STOPPED)

    def __str__(self):
        return self.name


class MotorLog(models.Model):
    motor = models.ForeignKey(Motor, on_delete=models.CASCADE)
    operator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    start_time = models.DateTimeField()
    stop_time = models.DateTimeField(null=True, blank=True)
    runtime_seconds = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_running(self):
        return self.stop_time is None

    def stop(self):
        if self.stop_time:
            raise ValidationError("Motor already stopped.")
        self.stop_time = timezone.now()
        self.runtime_seconds = int((self.stop_time - self.start_time).total_seconds())
        self.save(update_fields=["stop_time", "runtime_seconds"])


def start_motor(motor: Motor, operator):
    if motor.status == Motor.Status.RUNNING:
        raise ValidationError("Motor is already running.")
    active_log = MotorLog.objects.filter(motor=motor, stop_time__isnull=True).first()
    if active_log:
        raise ValidationError("Motor already has active session.")
    motor.status = Motor.Status.RUNNING
    motor.save(update_fields=["status"])
    return MotorLog.objects.create(motor=motor, operator=operator, start_time=timezone.now())


def stop_motor(motor: Motor):
    if motor.status != Motor.Status.RUNNING:
        raise ValidationError("Motor is not running.")
    log = MotorLog.objects.filter(motor=motor, stop_time__isnull=True).first()
    if not log:
        raise ValidationError("No active motor session found.")
    log.stop()
    motor.status = Motor.Status.STOPPED
    motor.save(update_fields=["status"])
    return log
