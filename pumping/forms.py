from django import forms

from .models import Motor


class MotorForm(forms.ModelForm):
    class Meta:
        model = Motor
        fields = ("name", "site", "status")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
