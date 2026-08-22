from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import AuditLog


class AuditListView(LoginRequiredMixin, ListView):
    model = AuditLog
    template_name = "audit/audit_list.html"
