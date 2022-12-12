from rest_framework import serializers
from .models import Gas, Video, Dron, Image


class GasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gas
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class DronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dron
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
