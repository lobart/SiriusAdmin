from django.contrib import admin
from .models import Profiles
import io
from django.core.files.images import ImageFile

def create_image_message(image_bytes, name):
    image = ImageFile(io.BytesIO(image_bytes), name=name)
    new_message = Profiles.objects.create(image=image)
    return new_message

@admin.register(Profiles)
class ProfilesAdmin(admin.ModelAdmin):
    list_display = ("employee_id", "full_name")
    fields = ("employee_id", "full_name")






