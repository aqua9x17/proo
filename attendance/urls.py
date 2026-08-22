from django.urls import path

from .views import (
    AttendanceCreateView,
    AttendanceListView,
    AttendanceUpdateView,
    EmployeeCreateView,
    EmployeeDeleteView,
    EmployeeListView,
    EmployeeUpdateView,
    check_in,
    check_out,
)

app_name = "attendance"

urlpatterns = [
    path("employees/", EmployeeListView.as_view(), name="employee_list"),
    path("employees/create/", EmployeeCreateView.as_view(), name="employee_create"),
    path("employees/<int:pk>/edit/", EmployeeUpdateView.as_view(), name="employee_update"),
    path("employees/<int:pk>/delete/", EmployeeDeleteView.as_view(), name="employee_delete"),
    path("records/", AttendanceListView.as_view(), name="attendance_list"),
    path("records/create/", AttendanceCreateView.as_view(), name="attendance_create"),
    path("records/<int:pk>/edit/", AttendanceUpdateView.as_view(), name="attendance_update"),
    path("employees/<int:employee_id>/check-in/", check_in, name="check_in"),
    path("employees/<int:employee_id>/check-out/", check_out, name="check_out"),
]
