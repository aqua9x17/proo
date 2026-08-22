from django.conf import settings
from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SiteMessage(models.Model):
    class Priority(models.TextChoices):
        NORMAL = "normal", "Normal"
        IMPORTANT = "important", "Important"
        URGENT = "urgent", "Urgent"

    title = models.CharField(max_length=200)
    message = models.TextField()
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    priority = models.CharField(max_length=20, choices=Priority.choices, default=Priority.NORMAL)
    expiry_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
