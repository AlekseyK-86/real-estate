from rest_framework import viewsets
from .models.flat import Flat
from .models.floor import Floor
from .models.section import Section
from .models.building import Building
from .models.project import Project
from .serializer import FlatSerializer, FloorSerializer, SectionSerializer, BuildingSerializer, ProjectSerializer

class FlatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Flat.objects.all()
    serializer_class = FlatSerializer

class FloorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

class SectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = SectionSerializer

class BuildingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = BuildingSerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = ProjectSerializer