from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.utils import timezone
from django.views.generic import TemplateView

from attendance.models import AttendanceRecord, Employee
from equipment.models import EquipmentItem
from pumping.models import Motor, MotorLog
from sites.models import SiteMessage


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.localdate()
        context.update(
            {
                "total_motors": Motor.objects.count(),
                "running_motors": Motor.objects.filter(status=Motor.Status.RUNNING).count(),
                "stopped_motors": Motor.objects.filter(status=Motor.Status.STOPPED).count(),
                "today_hours": round(
                    (MotorLog.objects.filter(start_time__date=today).aggregate(total=Sum("runtime_seconds"))["total"] or 0)
                    / 3600,
                    2,
                ),
                "employees_present": AttendanceRecord.objects.filter(date=today, status=AttendanceRecord.Status.PRESENT).count(),
                "equipment_count": EquipmentItem.objects.count(),
                "important_messages": SiteMessage.objects.filter(priority__in=[SiteMessage.Priority.IMPORTANT, SiteMessage.Priority.URGENT])[:5],
                "motors": Motor.objects.all(),
                "employees": Employee.objects.filter(is_active=True),
            }
        )
        return context
