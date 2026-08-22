from django.urls import path

from .views import EquipmentCreateView, EquipmentDeleteView, EquipmentListView, EquipmentUpdateView

app_name = "equipment"

urlpatterns = [
    path("", EquipmentListView.as_view(), name="equipment_list"),
    path("create/", EquipmentCreateView.as_view(), name="equipment_create"),
    path("<int:pk>/edit/", EquipmentUpdateView.as_view(), name="equipment_update"),
    path("<int:pk>/delete/", EquipmentDeleteView.as_view(), name="equipment_delete"),
]
