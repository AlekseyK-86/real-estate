from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from .selector import FlatSelector


class FlatListView(APIView):
    class FlatListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        square = serializers.FloatField()
        living_space = serializers.FloatField()
        kitchen_area = serializers.FloatField()
        rooms = serializers.IntegerField()
        status = serializers.CharField()
        price = serializers.IntegerField()
        description = serializers.CharField()
        photo = serializers.ImageField()
        floor_number=serializers.IntegerField()

    def get(self, request):
        flats = FlatSelector.get_all_flats()
        all_flats = self.FlatListSerializer(flats, many=True).data
        return Response(all_flats)


class FlatDetailView(APIView):
    class FlatDetailSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        square = serializers.FloatField()
        living_space = serializers.FloatField()
        kitchen_area = serializers.FloatField()
        rooms = serializers.IntegerField()
        status = serializers.CharField()
        price = serializers.IntegerField()
        description = serializers.CharField()
        photo = serializers.ImageField()
        floor_number=serializers.IntegerField()
        category_name=serializers.CharField()
        building_name=serializers.CharField()

    def get(self, request, flat_id):
        flat = FlatSelector.get_flat_by_id(flat_id)
        serializer = self.FlatDetailSerializer(flat).data
        return Response(serializer)
