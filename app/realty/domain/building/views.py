from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .selector import BuildingSelector


class BuildingListView(APIView):
    class BuildingListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        floors = serializers.IntegerField()
        name = serializers.CharField()
        photo = serializers.ImageField()
        date_of_construction = serializers.DateField()
        date_of_delivery = serializers.DateField()
        address = serializers.CharField()
        number = serializers.IntegerField()
        status = serializers.CharField()
        type = serializers.CharField()
        has_parking = serializers.BooleanField()
        elevators = serializers.IntegerField()
        project_name = serializers.CharField()

    def get(self, request):
        all_buildings = BuildingSelector.get_all_buildings()
        return Response(data=self.BuildingListSerializer(all_buildings, many=True).data)


class BuildingDetailView(APIView):
    class BuildingDetailSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        floors = serializers.IntegerField()
        name = serializers.CharField()
        photo = serializers.ImageField()
        date_of_construction = serializers.DateField()
        date_of_delivery = serializers.DateField()
        address = serializers.CharField()
        number = serializers.IntegerField()
        status = serializers.CharField()
        type = serializers.CharField()
        has_parking = serializers.BooleanField()
        elevators = serializers.IntegerField()
        project_name = serializers.CharField()
        total_flats = serializers.IntegerField()

    def get(self, request, building_id):
        building = BuildingSelector.get_building_detail(building_id)
        if not building:
            return Response({'error': 'Object does not exist'})

        return Response(data=self.BuildingDetailSerializer(building).data)
