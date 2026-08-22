from django.contrib import admin

from .models import AttendanceRecord, Employee

admin.site.register(Employee)
admin.site.register(AttendanceRecord)
