from django.urls import path

from .views import (
    MotorCreateView,
    MotorDeleteView,
    MotorListView,
    MotorLogListView,
    MotorUpdateView,
    motor_start_view,
    motor_stop_view,
)

app_name = "pumping"

urlpatterns = [
    path("", MotorListView.as_view(), name="motor_list"),
    path("create/", MotorCreateView.as_view(), name="motor_create"),
    path("<int:pk>/edit/", MotorUpdateView.as_view(), name="motor_update"),
    path("<int:pk>/delete/", MotorDeleteView.as_view(), name="motor_delete"),
    path("logs/", MotorLogListView.as_view(), name="motor_logs"),
    path("<int:pk>/start/", motor_start_view, name="motor_start"),
    path("<int:pk>/stop/", motor_stop_view, name="motor_stop"),
]
