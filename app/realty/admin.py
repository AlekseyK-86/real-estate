from django.contrib import admin

from realty.models.flat import Flat
from realty.models.floor import Floor
from realty.models.building import Building
from realty.models.project import Project
from realty.models.section import Section

class FlatAdmin(admin.ModelAdmin):
    list_display = (
        "price", 
        "status", 
        "category", 
        "square", 
        "rooms", 
        "living_space", 
        "kitchen_area",
        "photo",
        "get_floor_number",
        )
    search_fields = ("price", "category",)
    list_filter = ("status", ("category", admin.RelatedFieldListFilter), "rooms",)
    list_editable = ("status", "category",)

    def get_floor_number(self, obj):
        return obj.floor.number
    get_floor_number.short_description = 'Этаж' 

admin.site.register(Flat, FlatAdmin)


class FloorAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(Floor, FloorAdmin)


class SectionAdmin(admin.ModelAdmin):
    list_display = ("name", "number",)

admin.site.register(Section, SectionAdmin)


class BuildingAdmin(admin.ModelAdmin):
    list_display = (
        "name", 
        "floors", 
        "address", 
        "number", 
        "status", 
        "type", 
        "has_parking", 
        "elevators", 
        "get_project_name",
        "photo",
    )
    search_fields = ("address", "category",)
    list_filter = ("status", "type", "has_parking", "elevators", ("project", admin.RelatedFieldListFilter),)
    list_editable = ("status", "type", "has_parking", "elevators",)

    def get_project_name(self, obj):
        return obj.project.name
    
    get_project_name.short_description = 'Название проекта' 

admin.site.register(Building, BuildingAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "description","photo",)
    list_filter = ("name",)

admin.site.register(Project, ProjectAdmin)
