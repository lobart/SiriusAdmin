from django.contrib import admin
from .models import Profiles


@admin.register(Profiles)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ("employee_id", "full_name","drawing_data")
    fields = ("employee_id", "full_name", 'display_image')
    readonly_fields = ['display_image']




