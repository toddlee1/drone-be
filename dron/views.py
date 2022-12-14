from datetime import datetime, timedelta

from rest_framework import response
from rest_framework.exceptions import APIException
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import Gas, Video, Dron, Image
from rest_framework.viewsets import ModelViewSet
from .serializers import GasSerializer, VideoSerializer, DronSerializer, ImageSerializer


class GasViewSet(ModelViewSet):
    def list(self, request):
        # if request.GET.get('sensed') is None:
        #     queryset = Gas.objects.all()
        # else:
        #     sensed = int(request.GET.get('sensed'))
        #     start_at = datetime.fromtimestamp(sensed)
        #     end_at = datetime.fromtimestamp(sensed + 600)
        #     queryset = Gas.objects.filter(sensed__range=(start_at, end_at))
        if request.GET.get('video_id') is not None:
            video_id = request.GET.get('video_id')
            queryset = Gas.objects.filter(video_id=video_id)
        else:
            queryset = Gas.objects.all()

        if request.GET.get('size') is not None:
            size = request.GET.get('size')
            serializer = GasSerializer(queryset[:int(size)], many=True)
        else:
            serializer = GasSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        video_id = request.GET.get('video_id')
        queryset = Gas.objects.filter(video_id=video_id).latest('id')
        serializer = GasSerializer(queryset)
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


class DronViewSet(ModelViewSet):
    def list(self, request):
        queryset = Dron.objects.filter(id__range=[10001, 100000])
        serializer = DronSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, id=None, *args, **kwargs):
        queryset = Dron.objects.filter(id=id).first()
        serializer = DronSerializer(queryset)
        return Response(serializer.data)


class LiveViewSet(ModelViewSet):
    def list(self, request):
        queryset = Dron.objects.filter(id__range=[1, 100])
        serializer = DronSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, id=None, *args, **kwargs):
        queryset = Dron.objects.filter(id=id).first()
        serializer = DronSerializer(queryset)
        return Response(serializer.data)


class ImageViewSet(ModelViewSet):
    def list(self, request):
        if request.GET.get('video_id') is None:
            queryset = Image.objects.all()
        else:
            video_id = request.GET.get('video_id')
            queryset = Image.objects.filter(video_id=video_id)
        serializer = ImageSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, id=None, *args, **kwargs):
        queryset = Image.objects.filter(id=id).first()
        serializer = ImageSerializer(queryset)
        return Response(serializer.data)

    def update(self, request, id=None, *args, **kwargs):
        queryset = Image.objects.filter(id=id).first()
        serializer = ImageSerializer(queryset, data=JSONParser().parse(request), partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        raise APIException(400, serializer.errors)

