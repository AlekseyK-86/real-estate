from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from realty.models.building import Building


class BuildingSelector:
    @staticmethod
    def get_all_buildings():
        pass

    @staticmethod
    def get_building_detail(pk):
        pass
