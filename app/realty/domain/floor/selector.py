from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Count

from realty.domain.flat.entities import FlatEntity
from realty.domain.floor.entities import FloorEntity
from realty.models.floor import Floor
from typing import List

class FloorSelector:
    @staticmethod
    def get_floors_with_total_flats() -> List[FlatEntity]:
        floors = Floor.objects.annotate(total_flats=Count('flat'))
        return floors

    @staticmethod
    def query_set_to_dataclass(queryset, floor) -> List[FlatEntity]:
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
    def get_floor_detail(pk) -> List[FlatEntity]:
        try:
            """ flat_set: Это имя обратного отношения, через которое можно получить все объекты Flat, 
            связанные с конкретным объектом Floor. set подразумевает, 
            что к одному объекту Floor может соответствовать несколько объектов Flat."""
            floor = Floor.objects.prefetch_related(
                'flat_set__floor',
                'flat_set__category',
                'flat_set__building'
            ).get(id=pk) 
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            """ ObjectDoesNotExist - запрашиваемый объект не найден в базе данных
            MultipleObjectsReturned - запрос get() возвращает более одного объекта. 
            Метод get() предполагает, что результатом будет только один объект"""
            return None
        flats = floor.flat_set.all()

        data = FloorSelector.query_set_to_dataclass(flats, floor)

        return data
