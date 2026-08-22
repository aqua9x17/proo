from django import forms

from .models import AttendanceRecord, Employee


class StyledModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class EmployeeForm(StyledModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


class AttendanceForm(StyledModelForm):
    class Meta:
        model = AttendanceRecord
        fields = "__all__"
