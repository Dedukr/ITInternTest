from django.contrib import admin

from .form import CompanyForm
from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    form = CompanyForm  # Use the custom form
    list_display = (
        "name",
        "email",
        "phone",
    )  # Fields to display in the admin list view
    search_fields = ("name", "email")  # Fields to enable search functionality
    list_filter = ("user1", "user2", "user3")  # Fields to enable filtering


# Register your models here.
admin.site.register(Company, CompanyAdmin)
