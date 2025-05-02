from rest_framework import response
from typing import Any
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from category.models import Region
from .serializers import RegionSerializer


class RegionViewSet(ModelViewSet):
    permission_classes: list[Any] = [AllowAny, ]
    queryset = Region.objects.all()
    serializer_class = RegionSerializer