from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from accounts.mixins import RoleRequiredMixin
from accounts.models import User
from .forms import AttendanceForm, EmployeeForm
from .models import AttendanceRecord, Employee


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = "attendance/employee_list.html"


class EmployeeCreateView(RoleRequiredMixin, CreateView):
    allowed_roles = (User.Roles.ADMIN, User.Roles.MANAGER)
    model = Employee
    form_class = EmployeeForm
    template_name = "common/form.html"
    success_url = reverse_lazy("attendance:employee_list")


class EmployeeUpdateView(RoleRequiredMixin, UpdateView):
    allowed_roles = (User.Roles.ADMIN, User.Roles.MANAGER)
    model = Employee
    form_class = EmployeeForm
    template_name = "common/form.html"
    success_url = reverse_lazy("attendance:employee_list")


class EmployeeDeleteView(RoleRequiredMixin, DeleteView):
    allowed_roles = (User.Roles.ADMIN,)
    model = Employee
    template_name = "common/confirm_delete.html"
    success_url = reverse_lazy("attendance:employee_list")


class AttendanceListView(LoginRequiredMixin, ListView):
    model = AttendanceRecord
    template_name = "attendance/attendance_list.html"
    ordering = ("-date",)


class AttendanceCreateView(RoleRequiredMixin, CreateView):
    allowed_roles = (User.Roles.ADMIN, User.Roles.MANAGER, User.Roles.OPERATOR)
    model = AttendanceRecord
    form_class = AttendanceForm
    template_name = "common/form.html"
    success_url = reverse_lazy("attendance:attendance_list")


class AttendanceUpdateView(RoleRequiredMixin, UpdateView):
    allowed_roles = (User.Roles.ADMIN, User.Roles.MANAGER)
    model = AttendanceRecord
    form_class = AttendanceForm
    template_name = "common/form.html"
    success_url = reverse_lazy("attendance:attendance_list")


@login_required
@require_POST
def check_in(request, employee_id):
    if request.user.role not in (User.Roles.ADMIN, User.Roles.MANAGER, User.Roles.OPERATOR):
        return HttpResponseForbidden("Forbidden")
    employee = get_object_or_404(Employee, id=employee_id)
    record, _ = AttendanceRecord.objects.get_or_create(employee=employee, date=timezone.localdate())
    record.check_in = timezone.now()
    record.status = AttendanceRecord.Status.PRESENT
    record.save()
    return redirect("attendance:attendance_list")


@login_required
@require_POST
def check_out(request, employee_id):
    if request.user.role not in (User.Roles.ADMIN, User.Roles.MANAGER, User.Roles.OPERATOR):
        return HttpResponseForbidden("Forbidden")
    employee = get_object_or_404(Employee, id=employee_id)
    record, _ = AttendanceRecord.objects.get_or_create(employee=employee, date=timezone.localdate())
    record.check_out = timezone.now()
    record.save()
    return redirect("attendance:attendance_list")
