from django.contrib import admin

from .models import Site, SiteMessage

admin.site.register(Site)
admin.site.register(SiteMessage)
