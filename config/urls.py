from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("dashboard.urls")),
    path("accounts/", include("accounts.urls")),
    path("motors/", include("pumping.urls")),
    path("attendance/", include("attendance.urls")),
    path("equipment/", include("equipment.urls")),
    path("reports/", include("reports.urls")),
    path("sites/", include("sites.urls")),
    path("audit/", include("audit.urls")),
    path("settings/", include("core_settings.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
