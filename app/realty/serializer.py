from rest_framework.fields import Field
from rest_framework.serializers import Serializer
from rest_framework import serializers
from .models.flat import Flat
from .models.floor import Floor
from .models.section import Section
from .models.building import Building
from .models.project import Project

def serializer(
    name: str,
    fields: dict[str, Field],
    docstring: str = "",
    **kwargs,
) -> Serializer:
    serializer_class = type(name, (Serializer,), fields)
    serializer_class.__doc__ = docstring
    return serializer_class(**kwargs)

class FlatSerializer(serializers.ModelSerializer):
       class Meta:
           model = Flat
           fields = '__all__'

class FloorSerializer(serializers.ModelSerializer):
       class Meta:
           model = Floor
           fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
       class Meta:
           model = Section
           fields = '__all__'

class BuildingSerializer(serializers.ModelSerializer):
       class Meta:
           model = Building
           fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
       class Meta:
           model = Project
           fields = '__all__'
