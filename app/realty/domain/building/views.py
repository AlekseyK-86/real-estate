from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .selector import BuildingSelector


class BuildingListView(APIView):
    class ListBuildingSerializer(serializers.Serializer):
        pass


class BuildingDetailView(APIView):
    class DetailBuildingSerializer(serializers.Serializer):
        pass