import shutil
from pathlib import Path

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import FileResponse
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views import View
from django.views.generic import UpdateView

from .forms import CompanySettingsForm
from .models import CompanySettings


class CompanySettingsView(LoginRequiredMixin, UpdateView):
    model = CompanySettings
    form_class = CompanySettingsForm
    template_name = "core_settings/company_settings.html"
    success_url = reverse_lazy("core_settings:company_settings")

    def get_object(self, queryset=None):
        return CompanySettings.objects.first() or CompanySettings.objects.create()

    def dispatch(self, request, *args, **kwargs):
        if request.user.role != "admin" and not request.user.is_superuser:
            return HttpResponseForbidden("Forbidden")
        return super().dispatch(request, *args, **kwargs)


class BackupDatabaseView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.role != "admin" and not request.user.is_superuser:
            return HttpResponseForbidden("Forbidden")
        backup_dir = Path(settings.BASE_DIR) / "media" / "backups"
        backup_dir.mkdir(parents=True, exist_ok=True)
        backup_path = backup_dir / "db_backup.sqlite3"
        shutil.copy(settings.BASE_DIR / "db.sqlite3", backup_path)
        return FileResponse(open(backup_path, "rb"), as_attachment=True, filename=backup_path.name)


class RestoreDatabaseView(LoginRequiredMixin, View):
    @require_POST
    def post(self, request):
        if request.user.role != "admin" and not request.user.is_superuser:
            return HttpResponseForbidden("Forbidden")
        upload = request.FILES.get("backup_file")
        if upload:
            with open(settings.BASE_DIR / "db.sqlite3", "wb") as target:
                for chunk in upload.chunks():
                    target.write(chunk)
            messages.success(request, "Database restored successfully.")
        else:
            messages.error(request, "Please upload backup file.")
        return redirect("core_settings:company_settings")
