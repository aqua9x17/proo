from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from accounts.mixins import RoleRequiredMixin
from accounts.models import User
from .forms import MotorForm
from .models import Motor, MotorLog, start_motor, stop_motor


class MotorListView(LoginRequiredMixin, ListView):
    model = Motor
    template_name = "pumping/motor_list.html"


class MotorCreateView(RoleRequiredMixin, CreateView):
    allowed_roles = (User.Roles.ADMIN, User.Roles.MANAGER)
    model = Motor
    form_class = MotorForm
    template_name = "common/form.html"
    success_url = reverse_lazy("pumping:motor_list")


class MotorUpdateView(RoleRequiredMixin, UpdateView):
    allowed_roles = (User.Roles.ADMIN, User.Roles.MANAGER)
    model = Motor
    form_class = MotorForm
    template_name = "common/form.html"
    success_url = reverse_lazy("pumping:motor_list")


class MotorDeleteView(RoleRequiredMixin, DeleteView):
    allowed_roles = (User.Roles.ADMIN,)
    model = Motor
    template_name = "common/confirm_delete.html"
    success_url = reverse_lazy("pumping:motor_list")


class MotorLogListView(LoginRequiredMixin, ListView):
    model = MotorLog
    template_name = "pumping/motor_log_list.html"
    ordering = ("-start_time",)


@login_required
@require_POST
def motor_start_view(request, pk):
    if request.user.role not in (User.Roles.ADMIN, User.Roles.MANAGER, User.Roles.OPERATOR):
        return HttpResponseForbidden("Forbidden")
    motor = get_object_or_404(Motor, pk=pk)
    try:
        start_motor(motor, request.user)
        messages.success(request, f"{motor.name} started.")
    except ValidationError as exc:
        messages.error(request, str(exc))
    return redirect("pumping:motor_list")


@login_required
@require_POST
def motor_stop_view(request, pk):
    if request.user.role not in (User.Roles.ADMIN, User.Roles.MANAGER, User.Roles.OPERATOR):
        return HttpResponseForbidden("Forbidden")
    motor = get_object_or_404(Motor, pk=pk)
    try:
        stop_motor(motor)
        messages.success(request, f"{motor.name} stopped.")
    except ValidationError as exc:
        messages.error(request, str(exc))
    return redirect("pumping:motor_list")
