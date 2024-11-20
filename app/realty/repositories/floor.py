from typing import List

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Count

from realty.domain.flat.entities import FlatEntity
from realty.domain.floor.entities import FloorEntity
from realty.models.floor import Floor

class FloorRepository:

    @staticmethod
    def fetch_all_floors() -> List[FloorEntity]:
        floors = Floor.objects.annotate(total_flats=Count('flat'))

        return floors
    
    @staticmethod
    def query_set_to_dataclass(queryset, floor) -> FloorEntity:
        return FloorEntity(
            id=floor.id,
            name=floor.name,
            number=floor.number,
            flats=[
                FlatEntity(
                    id=flat.id,
                    square=flat.square,
                    living_space=flat.living_space,
                    kitchen_area=flat.kitchen_area,
                    rooms=flat.rooms,
                    status=flat.status,
                    price=flat.price,
                    description=flat.description,
                    photo=flat.photo,
                    floor_number=flat.floor.number,
                    category_name=flat.category.name,
                    building_name=flat.building.name
                )
                for flat in queryset
            ]
        )
    
    @staticmethod
    def fetch_floor_detail(pk) -> FloorEntity:
        try:
            floor = Floor.objects.prefetch_related(
                'flat_set__floor',
                'flat_set__category',
                'flat_set__building'
            ).get(id=pk)

        except ObjectDoesNotExist:
            raise ObjectDoesNotExist(f"Объект c id={pk} в модели Floor не найден.")
        
        except MultipleObjectsReturned:
            raise MultipleObjectsReturned(f"Что то пошло не так, из модели Floor вернулось более чем один объект.")
        
        flats = floor.flat_set.all()
        data = FloorRepository.query_set_to_dataclass(flats, floor)

        return data