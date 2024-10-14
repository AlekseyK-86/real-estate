from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .selector import SectionSelector
from ...serializer import serializer


class SectionListView(APIView):
    class SectionListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        number = serializers.IntegerField()

    def get(self, request):
        all_sections = SectionSelector.get_all_sections()        
        return Response(data = self.SectionListSerializer(all_sections, many=True).data)


class SectionDetailView(APIView):
    class SectionDetailSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        number = serializers.IntegerField()

    def get(self, request, section_id):
        section = SectionSelector.get_section_detail(section_id)
        if not section:
            return Response({'error': 'Object does not exist'})
        return Response(data=self.SectionDetailSerializer(section).data)
