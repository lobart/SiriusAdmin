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
    list_display = ("employee_id", "full_name","drawing_data")
    fields = ("employee_id", "full_name")

    def render_change_form(self, request, context, *args, **kwargs):
        context['image'] = create_image_message(context['drawing_data'], context['employee_id'] + '.jpg')
        return super(ProfilesAdmin, self).render_change_form(request, context, args, kwargs)




