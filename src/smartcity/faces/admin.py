from django.contrib import admin
from .models import Profiles
from django.forms import ModelForm
# Register your models here.

@admin.register(Profiles)
class ProfilesAdmin(admin.ModelAdmin, ModelForm):
    list_display = ("employee_id", "full_name",)
    fields = ("employee_id", "full_name", "drawing_data")
    list_editable = ("drawing_data",)