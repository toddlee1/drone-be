from django.db import models


class Gas(models.Model):
    id = models.BigAutoField(primary_key=True)
    oxy = models.CharField(max_length=10)
    sensed = models.DateTimeField()
    video_id = models.IntegerField()

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


class Dron(models.Model):
    id = models.BigAutoField(primary_key=True)
    facility_name = models.CharField(max_length=255)
    image_type = models.CharField(max_length=10)
    video_url = models.CharField(max_length=255)
    ir_video_url = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    length = models.CharField(max_length=10)
    site_id = models.IntegerField()
    dron_id = models.IntegerField()
    dron_name = models.CharField(max_length=20)
    battery = models.IntegerField()
    sensor_type = models.CharField(max_length=20)
    optime = models.TimeField()
    altitude = models.IntegerField()
    lat = models.FloatField()
    lon = models.FloatField()
    site_name = models.CharField(max_length=50)
    admin_name = models.CharField(max_length=50)
    rate1 = models.IntegerField()
    rate2 = models.IntegerField()

    class Meta:
        db_table = 'DronInfo'
        ordering = ['id']


class Image(models.Model):
    id = models.BigAutoField(primary_key=True)
    image_url = models.CharField(max_length=255)
    video_id = models.IntegerField()

    class Meta:
        db_table = 'DronImage'
        ordering = ['id']