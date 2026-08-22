from .models import CompanySettings


def company_settings(_request):
    return {"company_settings": CompanySettings.objects.first()}
