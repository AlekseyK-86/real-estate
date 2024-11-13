from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .selector import FloorSelector
from realty.models.flat import Flat
from realty.inline_serializer import inline_serializer


class FloorListView(APIView):
    class FloorListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        number = serializers.IntegerField()
        total_flats = serializers.IntegerField()

    def get(self, request):
        all_floors = FloorSelector.get_floors_with_total_flats()
        return Response(data=self.FloorListSerializer(all_floors, many=True).data)


class FloorDetailView(APIView):
    class FloorDetailSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        number = serializers.IntegerField()
        flats = inline_serializer(
            name='Flats',
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
        floor = FloorSelector.get_floor_detail(pk)
        if not floor:
            return Response({'error': 'Object does not exist'})

        return Response(data=self.FloorDetailSerializer(floor).data)
