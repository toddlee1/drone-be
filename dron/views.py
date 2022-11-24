from datetime import datetime, timedelta

from rest_framework.response import Response
from .models import Gas, Video
from rest_framework.viewsets import ModelViewSet
from .serializers import GasSerializer, VideoSerializer


class GasViewSet(ModelViewSet):
    def list(self, request):
        if request.GET.get('sensed') is None:
            queryset = Gas.objects.all()
        else:
            sensed = int(request.GET.get('sensed'))
            start_at = datetime.fromtimestamp(sensed)
            end_at = datetime.fromtimestamp(sensed + 600)
            queryset = Gas.objects.filter(sensed__range=(start_at, end_at))
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

