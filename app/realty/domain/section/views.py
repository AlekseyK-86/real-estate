from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .selector import SectionSelector
from realty.models.flat import Flat
from realty.inline_serializer import inline_serializer


class SectionListView(APIView):
    class SectionListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        number = serializers.IntegerField()
        total_flats = serializers.IntegerField()

    def get(self, request):
        all_floors = SectionSelector.get_sections_with_total_flats()
        return Response(data=self.SectionListSerializer(all_floors, many=True).data)


class SectionDetailView(APIView):
    class SectionDetailSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        number = serializers.IntegerField()
        flats = inline_serializer(
            name='Section',
            fields={
                'id': serializers.IntegerField(),
                'square': serializers.FloatField(),
                'living_space': serializers.FloatField(),
                'kitchen_area': serializers.FloatField(),
                'rooms': serializers.IntegerField(),
                'status': serializers.CharField(),
                'price': serializers.IntegerField(),
                'description': serializers.CharField(),
                'photo': serializers.ImageField(),
                'floor_number': serializers.IntegerField(),
                'category_name': serializers.CharField(),
                'building_name': serializers.CharField()
            },
            docstring = "Получение списка квартир на этаже",
            many=True
        )

    def get(self, request, pk):
        section = SectionSelector.get_section_detail(pk)
        if not section:
            return Response({'error': 'Object does not exist'})

        return Response(data=self.SectionDetailSerializer(section).data)
