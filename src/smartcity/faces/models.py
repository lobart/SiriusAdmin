from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils.html import mark_safe
from django.utils.functional import cached_property
from django.utils.html import format_html

import io
import logging
logger = logging.getLogger(__name__)
logger.info(__name__)

class Cameras(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.CharField(_('url'), max_length=255)
    description = models.CharField(_('description'), max_length=255)

    class Meta:
        verbose_name = _('cameras')
        verbose_name_plural = _('cameras')
        db_table = "public\".\"cameras"


class Profiles(models.Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        name = '{id}'.format(id=self.employee_id) + '.jpg'
        if self.drawing_data is not None:
            self.image = models.FileField(io.BytesIO(bytes(self.drawing_data)), name=name, upload_to=str(settings.MEDIA_ROOT))


    id = models.IntegerField(primary_key=True)
    employee_id = models.IntegerField(unique=True)
    full_name = models.TextField()
    drawing_data = models.BinaryField(null=True, editable=True)

    @cached_property
    def display_image(self):
        html = '<img src="{img}">'
        logger.info(self.image)
        if self.image:
            return format_html(html, img=self.image.url)
        return format_html('<strong>There is no image for this entry.<strong>')
    display_image.short_description = 'Display image'

    class Meta:
        verbose_name = _('profiles')
        verbose_name_plural = _('profiles')
        db_table = "public\".\"profiles"


class FaceDescriptors(models.Model):
    id = models.BigIntegerField(primary_key=True)
    descriptor = models.TextField()
    status = models.TextField()
    profile_id = models.ForeignKey(Profiles, on_delete=models.SET_NULL, null=True)
    descriptor_distance = models.FloatField(null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = _('face descriptors')
        verbose_name_plural = _('face descriptors')
        db_table = "public\".\"face_descriptors"


class CapturedFaces(models.Model):
    id = models.BigIntegerField(primary_key=True)
    file_id = models.IntegerField()
    camera_id = models.ForeignKey(Cameras, on_delete=models.SET_NULL, null=True)
    percent = models.FloatField()
    bbox = models.TextField()
    clusterized = models.BooleanField()
    descriptor_id = models.ForeignKey(FaceDescriptors, on_delete=models.SET_NULL, null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    descriptor_status = models.TextField(null=True)
    variance = models.FloatField(null=True)

    class Meta:
        verbose_name = _('cameras')
        verbose_name_plural = _('cameras')
        db_table = "public\".\"captured_faces"


class Whitelist(models.Model):
    id = models.IntegerField(primary_key=True)
    employee_id = models.IntegerField(unique=True)
    full_name = models.TextField()

    class Meta:
        verbose_name = _('whitelist')
        verbose_name_plural = _('whitelist')
        db_table = "public\".\"whitelist"


class ExemplarDescriptors(models.Model):
    id = models.IntegerField(primary_key=True)
    profile_id = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True)
    descriptor = models.TextField()

    class Meta:
        verbose_name = _('exemplar descriptors')
        verbose_name_plural = _('exemplar descriptors')
        db_table = "public\".\"exemplar_descriptors"


class ExemplarDescriptorsBackup(models.Model):
    id = models.IntegerField(primary_key=True)
    profile_id = models.ForeignKey(Profiles, on_delete=models.CASCADE, null=True)
    descriptor = models.TextField()

    class Meta:
        verbose_name = _('exemplar descriptors backup')
        verbose_name_plural = _('exemplar descriptors backup')
        db_table = "public\".\"exemplar_descriptors_backup"
