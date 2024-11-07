from django.contrib import admin
from realty.models.flat import Flat
from realty.models.floor import Floor
from realty.models.building import Building
from realty.models.project import Project

class FlatAdmin(admin.ModelAdmin):
    list_display = ("price", "status", "category", "square", "rooms", "living_space", "kitchen_area",)
    search_fields = ("price", "category",)
    list_filter = ("status", ("category", admin.RelatedFieldListFilter), "rooms",)
    list_editable = ("status",)


class FloorAdmin(admin.ModelAdmin):
    list_display = ["name"]

class SectionAdmin(admin.ModelAdmin):
    list_display = ["name", "number"]

class BuildingAdmin(admin.ModelAdmin):
    list_display = ["name", "floors", "address", "number", "status", "type", "has_parking", "elevators"]
    search_fields = ("address", "category",)
    list_filter = ("status", "type", "has_parking", "elevators",)
    list_editable = ("status",)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]

admin.site.register(Flat, FlatAdmin)
admin.site.register(Floor, FloorAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Project, ProjectAdmin)
