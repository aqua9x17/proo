from django.urls import path

from .views import BackupDatabaseView, CompanySettingsView, RestoreDatabaseView

app_name = "core_settings"

urlpatterns = [
    path("company/", CompanySettingsView.as_view(), name="company_settings"),
    path("backup/", BackupDatabaseView.as_view(), name="backup_database"),
    path("restore/", RestoreDatabaseView.as_view(), name="restore_database"),
]
