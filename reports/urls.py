from django.urls import path

from .views import (
    AttendanceReportExcelView,
    AttendanceReportPDFView,
    EquipmentReportExcelView,
    EquipmentReportPDFView,
    MotorReportExcelView,
    MotorReportPDFView,
    ReportIndexView,
)

app_name = "reports"

urlpatterns = [
    path("", ReportIndexView.as_view(), name="index"),
    path("motors/pdf/", MotorReportPDFView.as_view(), name="motor_pdf"),
    path("motors/excel/", MotorReportExcelView.as_view(), name="motor_excel"),
    path("attendance/pdf/", AttendanceReportPDFView.as_view(), name="attendance_pdf"),
    path("attendance/excel/", AttendanceReportExcelView.as_view(), name="attendance_excel"),
    path("equipment/pdf/", EquipmentReportPDFView.as_view(), name="equipment_pdf"),
    path("equipment/excel/", EquipmentReportExcelView.as_view(), name="equipment_excel"),
]
