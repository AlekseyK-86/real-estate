from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .selector import ProjectSelector
from realty.inline_serializer import inline_serializer


class ProjectListView(APIView):
    class ProjectListSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        description = serializers.CharField()
        photo = serializers.ImageField()

    def get(self, request):
        all_projects = ProjectSelector.get_all_projects()
        data = self.ProjectListSerializer(all_projects, many=True).data
        return Response(data)


class ProjectDetailView(APIView):
    class ProjectDetailSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        name = serializers.CharField()
        description = serializers.CharField()
        photo = serializers.ImageField()
        buildings = inline_serializer(
            name='Buildings',
            fields={
                'id': serializers.IntegerField(),
                'floors': serializers.IntegerField(),
                'name': serializers.CharField(),
                'photo': serializers.ImageField(),
                'date_of_construction': serializers.DateField(),
                'date_of_delivery': serializers.DateField(),
                'address': serializers.CharField(),
                'number': serializers.IntegerField(),
                'status': serializers.CharField(),
                'type': serializers.CharField(),
                'has_parking': serializers.BooleanField(),
                'elevators': serializers.IntegerField(),
                'project_name': serializers.CharField()
            },
            many=True
        )

    def get(self, request, project_id):
        project = ProjectSelector.get_project_detail(project_id)

        return Response(data=self.ProjectDetailSerializer(project).data)
