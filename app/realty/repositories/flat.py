from typing import List

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from realty.domain.flat.entities import FlatEntity
from realty.models.flat import Flat


class FlatRepository:

    @staticmethod
    def fetch_all_flats() -> List[FlatEntity]:
        flats = Flat.objects.all().select_related('floor', 'category', 'building')
        data = FlatRepository.query_set_all_to_dataclass(flats)

        return data

    @staticmethod
    def query_set_all_to_dataclass(queryset) -> List[FlatEntity]:
        return [
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

    @staticmethod
    def fetch_flat_detail(pk) -> FlatEntity:
        try:
            flat = Flat.objects.select_related('floor', 'category', 'building').get(id=pk)

        except ObjectDoesNotExist:
            raise ObjectDoesNotExist(f"Объект c id={pk} в модели Flat не найден.")
        
        except MultipleObjectsReturned:
            raise MultipleObjectsReturned(f"Что то пошло не так, из модели Flat вернулось более чем один объект.")
        
        data = FlatEntity(
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

        return data