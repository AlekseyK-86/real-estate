from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from realty.domain.flat.entities import FlatEntity
from realty.models.flat import Flat

from typing import List

from drf_spectacular.utils import extend_schema


class FlatSelector:

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
    #@extend_schema(summary="API для получение всех квартир ")
    def get_all_flats():
        flats = Flat.objects.all().select_related('floor', 'category', 'building')
        data = FlatSelector.query_set_all_to_dataclass(flats)
        return data


    @staticmethod
    #@extend_schema(summary="API для получение одной квартир ")
    def get_flat_by_id(flat_id) -> List[FlatEntity]:
        try:
            flat = Flat.objects.select_related('floor', 'category', 'building').get(id=flat_id)
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            return None

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
