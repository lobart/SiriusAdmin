import io
from django.core.files.images import ImageFile
from .models import Profiles
from django.views.generic.detail import DetailView


def create_image_message(image_bytes, name):
    image = ImageFile(io.BytesIO(image_bytes), name=name)
    new_message = Profiles.objects.create(image=image)
    return  new_message


class PersonDetailView(DetailView):

    model = Profiles

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image'] = create_image_message( context['drawing_data'], context['employee_id'] + '.jpg' )
        return context
