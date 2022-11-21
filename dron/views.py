from rest_framework.response import Response
from .models import Gas, Video
from rest_framework.viewsets import ModelViewSet
from .serializers import GasSerializer, VideoSerializer


class GasViewSet(ModelViewSet):
    def get(self, request):
        queryset = Gas.objects.all()
        serializer = GasSerializer(queryset, many=True)
        return Response(serializer.data)


class VideoViewSet(ModelViewSet):
    def list(self, request):
        queryset = Video.objects.all()
        serializer = VideoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, id=None, *args, **kwargs):
        queryset = Video.objects.filter(id=id).first()
        serializer = VideoSerializer(queryset)
        return Response(serializer.data)

