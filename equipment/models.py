from django.db import models

from sites.models import Site


class EquipmentItem(models.Model):
    class Category(models.TextChoices):
        EXTRA_MOTOR = "extra_motor", "Extra Motor"
        LIGHT = "light", "Light"
        PIPE = "pipe", "Pipe"
        CABLE = "cable", "Cable"
        STARTER = "starter", "Starter"
        VALVE = "valve", "Valve"
        PUMP = "pump", "Pump"
        TOOLS = "tools", "Tools"
        OTHER = "other", "Other Material"

    item_name = models.CharField(max_length=150)
    category = models.CharField(max_length=20, choices=Category.choices)
    quantity = models.PositiveIntegerField(default=1)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    location = models.CharField(max_length=200, blank=True)
    condition = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=100, blank=True)
    remarks = models.TextField(blank=True)
    photo = models.ImageField(upload_to="equipment/", blank=True, null=True)

    def __str__(self):
        return self.item_name
