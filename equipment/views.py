from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from accounts.mixins import RoleRequiredMixin
from accounts.models import User
from .forms import EquipmentForm
from .models import EquipmentItem


class EquipmentListView(LoginRequiredMixin, ListView):
    model = EquipmentItem
    template_name = "equipment/equipment_list.html"


class EquipmentCreateView(RoleRequiredMixin, CreateView):
    allowed_roles = (User.Roles.ADMIN, User.Roles.MANAGER)
    model = EquipmentItem
    form_class = EquipmentForm
    template_name = "common/form.html"
    success_url = reverse_lazy("equipment:equipment_list")


class EquipmentUpdateView(RoleRequiredMixin, UpdateView):
    allowed_roles = (User.Roles.ADMIN, User.Roles.MANAGER)
    model = EquipmentItem
    form_class = EquipmentForm
    template_name = "common/form.html"
    success_url = reverse_lazy("equipment:equipment_list")


class EquipmentDeleteView(RoleRequiredMixin, DeleteView):
    allowed_roles = (User.Roles.ADMIN,)
    model = EquipmentItem
    template_name = "common/confirm_delete.html"
    success_url = reverse_lazy("equipment:equipment_list")
