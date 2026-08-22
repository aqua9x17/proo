from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import View

from attendance.models import AttendanceRecord
from equipment.models import EquipmentItem
from pumping.models import MotorLog

from .utils import export_simple_excel, export_simple_pdf


class MotorReportPDFView(LoginRequiredMixin, View):
    def get(self, _request):
        rows = MotorLog.objects.values_list("motor__name", "operator__username", "start_time", "stop_time", "runtime_seconds")
        response = export_simple_pdf("Motor Report", rows)
        response["Content-Disposition"] = "attachment; filename=motor_report.pdf"
        return response


class MotorReportExcelView(LoginRequiredMixin, View):
    def get(self, _request):
        rows = MotorLog.objects.values_list("motor__name", "operator__username", "start_time", "stop_time", "runtime_seconds")
        response = export_simple_excel("MotorLogs", ["Motor", "Operator", "Start", "Stop", "Runtime(s)"], rows)
        response["Content-Disposition"] = "attachment; filename=motor_report.xlsx"
        return response


class AttendanceReportPDFView(LoginRequiredMixin, View):
    def get(self, _request):
        rows = AttendanceRecord.objects.values_list("employee__name", "date", "status", "check_in", "check_out")
        response = export_simple_pdf("Attendance Report", rows)
        response["Content-Disposition"] = "attachment; filename=attendance_report.pdf"
        return response


class AttendanceReportExcelView(LoginRequiredMixin, View):
    def get(self, _request):
        rows = AttendanceRecord.objects.values_list("employee__name", "date", "status", "check_in", "check_out")
        response = export_simple_excel("Attendance", ["Employee", "Date", "Status", "Check In", "Check Out"], rows)
        response["Content-Disposition"] = "attachment; filename=attendance_report.xlsx"
        return response


class EquipmentReportPDFView(LoginRequiredMixin, View):
    def get(self, _request):
        rows = EquipmentItem.objects.values_list("item_name", "category", "quantity", "site__name", "status")
        response = export_simple_pdf("Equipment Report", rows)
        response["Content-Disposition"] = "attachment; filename=equipment_report.pdf"
        return response


class EquipmentReportExcelView(LoginRequiredMixin, View):
    def get(self, _request):
        rows = EquipmentItem.objects.values_list("item_name", "category", "quantity", "site__name", "status")
        response = export_simple_excel("Equipment", ["Item", "Category", "Qty", "Site", "Status"], rows)
        response["Content-Disposition"] = "attachment; filename=equipment_report.xlsx"
        return response


class ReportIndexView(LoginRequiredMixin, View):
    def get(self, _request):
        return HttpResponse("Use report export links from navigation.")
