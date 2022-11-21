from django.db import models


class Gas(models.Model):
    id = models.BigAutoField(primary_key=True)
    oxy = models.CharField(max_length=10)
    sensed = models.DateTimeField()

    class Meta:
        db_table = 'DronGas'


class Video(models.Model):
    id = models.BigAutoField(primary_key=True)
    video_url = models.CharField(max_length=255)
    ir_video_url = models.CharField(max_length=255)
    site_name = models.CharField(max_length=255)
    facility_name = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'DronVideo'
        ordering = ['created_at']
