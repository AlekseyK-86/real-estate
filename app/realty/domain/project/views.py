from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .selector import ProjectSelector
from realty.inline_serializer import inline_serializer


class ProjectListView(APIView):
    class ProjectListSerializer(serializers.Serializer):
        pass


class ProjectDetailView(APIView):
    class ProjectDetailSerializer(serializers.Serializer):
        pass
