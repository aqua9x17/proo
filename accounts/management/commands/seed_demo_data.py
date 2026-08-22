from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from attendance.models import Employee
from core_settings.models import CompanySettings
from equipment.models import EquipmentItem
from pumping.models import Motor
from sites.models import Site, SiteMessage


class Command(BaseCommand):
    help = "Seed demo data for Unity Infra app"

    def handle(self, *args, **options):
        User = get_user_model()

        admin, _ = User.objects.get_or_create(username="admin", defaults={"role": "admin", "is_staff": True, "is_superuser": True})
        admin.set_password("admin@123")
        admin.save()

        manager, _ = User.objects.get_or_create(username="manager", defaults={"role": "manager", "is_staff": True})
        manager.set_password("manager@123")
        manager.save()

        operator, _ = User.objects.get_or_create(username="operator", defaults={"role": "operator"})
        operator.set_password("operator@123")
        operator.save()

        site, _ = Site.objects.get_or_create(name="Main Site", defaults={"location": "Chennai"})

        for index in range(1, 5):
            Motor.objects.get_or_create(name=f"Motor {index}", site=site)

        Employee.objects.get_or_create(name="Ravi Kumar", employee_code="EMP001", site=site)
        EquipmentItem.objects.get_or_create(item_name="Backup Pump", category="pump", site=site, defaults={"quantity": 2})

        SiteMessage.objects.get_or_create(
            title="Pump Maintenance",
            site=site,
            defaults={
                "message": "Service line #2 tomorrow morning.",
                "priority": "important",
                "created_by": admin,
            },
        )

        CompanySettings.objects.get_or_create(company_name="Unity Infra")

        self.stdout.write(self.style.SUCCESS("Demo data seeded successfully."))
