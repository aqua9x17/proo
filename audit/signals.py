from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from attendance.models import AttendanceRecord, Employee
from equipment.models import EquipmentItem
from pumping.models import Motor, MotorLog
from sites.models import Site, SiteMessage

from .models import AuditLog


def create_log(instance, action):
    AuditLog.objects.create(
        action=action,
        model_name=instance.__class__.__name__,
        object_id=str(instance.pk),
        details=str(instance),
    )


for model in [Site, SiteMessage, Motor, MotorLog, Employee, AttendanceRecord, EquipmentItem]:

    @receiver(post_save, sender=model)
    def _save_receiver(sender, instance, created, **kwargs):
        create_log(instance, "created" if created else "updated")

    @receiver(post_delete, sender=model)
    def _delete_receiver(sender, instance, **kwargs):
        create_log(instance, "deleted")
