from django import forms

from .models import Site, SiteMessage


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class SiteForm(BootstrapModelForm):
    class Meta:
        model = Site
        fields = "__all__"


class SiteMessageForm(BootstrapModelForm):
    class Meta:
        model = SiteMessage
        exclude = ("created_by",)
