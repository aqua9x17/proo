from django.db import models


class CompanySettings(models.Model):
    company_name = models.CharField(max_length=150, default="Unity Infra")
    address = models.CharField(max_length=255, blank=True)
    contact = models.CharField(max_length=80, blank=True)
    report_footer = models.CharField(max_length=255, blank=True)
    logo = models.ImageField(upload_to="company/", null=True, blank=True)

    def __str__(self):
        return self.company_name
