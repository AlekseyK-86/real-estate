from typing import List

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Count

from realty.domain.flat.entities import FlatEntity
from realty.models.floor import Floor

class FloorRepository:
    @staticmethod
    def fetch_all_floors() -> List[FlatEntity]:
        return Floor.objects.annotate(total_flats=Count('flat'))

    @staticmethod
    def fetch_floor_detail(pk) -> List[FlatEntity]:        
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

        return (flats, floor)