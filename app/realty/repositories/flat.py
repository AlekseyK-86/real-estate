from typing import List

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from realty.domain.flat.entities import FlatEntity
from realty.models.flat import Flat


class FlatRepository:
    @staticmethod
    def fetch_all_flats() -> List[FlatEntity]:
        return Flat.objects.all().select_related('floor', 'category', 'building')

    @staticmethod
    def fetch_flat_detail(pk) -> List[FlatEntity]:
        try:
            flat = Flat.objects.select_related('floor', 'category', 'building').get(id=pk)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist(f"Объект c id={pk} в модели Flat не найден.")
        
        except MultipleObjectsReturned:
            raise MultipleObjectsReturned(f"Что то пошло не так, из модели Flat вернулось более чем один объект.")

        return flat