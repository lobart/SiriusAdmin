from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

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

    id = models.IntegerField(primary_key=True)
    employee_id = models.IntegerField(unique=True)
    full_name = models.TextField()
    drawing_data = models.BinaryField(null=True, editable=True)

    def __str__(self):
        name = '{id}'.format(id=self.employee_id) + '.jpg'
        image = models.FileField(io.BytesIO(bytes(self.drawing_data)), name=name,
                                      upload_to=str(settings.MEDIA_ROOT), null=True)
        storage = image.storage.location
        data = image.description
        if image:
            logger.info(image)
            return "Image url is %s" % image.url
        return "Not image url"


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
