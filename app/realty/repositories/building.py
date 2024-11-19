from typing import List

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from realty.domain.building.entities import BuildingDetailEntity, BuildingEntity
from realty.models.building import Building

class BuildingRepository:
    @staticmethod
    def fetch_all_buildings() -> List[BuildingEntity]:
        return Building.objects.select_related('project').all()

    @staticmethod
    def fetch_building_detail(pk) -> List[BuildingDetailEntity]:
        try:
            building = Building.objects.prefetch_related(
                'flat_set__floor',
                'flat_set__category',
                'flat_set__building'
            ).get(id=pk)

        except ObjectDoesNotExist:
            raise ObjectDoesNotExist(f"Объект c id={pk} в модели Building не найден.")
        
        except MultipleObjectsReturned:
            raise MultipleObjectsReturned(f"Что то пошло не так, из модели Building вернулось более чем один объект.")
        
        total_flats = building.flat_set.count()

        return (building, total_flats)