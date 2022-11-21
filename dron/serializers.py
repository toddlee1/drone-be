from rest_framework import serializers
from .models import Gas, Video


class GasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gas
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
