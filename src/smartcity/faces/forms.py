from django.forms import ModelForm
from .models import Profiles


class UploadImageForm(ModelForm):
    class Meta:
        model = Profiles
        fields = ['drawing_data']