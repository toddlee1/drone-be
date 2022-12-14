"""drone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dron.views import GasViewSet, VideoViewSet, DronViewSet, ImageViewSet, LiveViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dron/gas', GasViewSet.as_view({'get': 'list'})),
    path('dron/gas/latest', GasViewSet.as_view({'get': 'retrieve'})),
    path('dron/videos', VideoViewSet.as_view(actions={'get': 'list'}), name='video'),
    path('dron/video/<int:id>', VideoViewSet.as_view(actions={'get': 'retrieve'}), name='video'),
    path('dron/list', DronViewSet.as_view(actions={'get': 'list'}), name='dron'),
    path('dron/detail/<int:id>', DronViewSet.as_view(actions={'get': 'retrieve'}), name='dron'),
    path('dron/live/list', LiveViewSet.as_view(actions={'get': 'list'}), name='live'),
    path('dron/image/list', ImageViewSet.as_view(actions={'get': 'list'}), name='image'),
    path('dron/image/detail/<int:id>', ImageViewSet.as_view(actions={'get': 'retrieve'}), name='image'),
    path('dron/image/modify/<int:id>', ImageViewSet.as_view(actions={'put': 'update'}), name='image')
]
