from django.contrib import admin
from .models import Profiles
# Register your models here.

@admin.register(Profiles)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ("employee_id", "full_name")
    fields = ("employee_id", "full_name")
    list_filter = ("full_name",)