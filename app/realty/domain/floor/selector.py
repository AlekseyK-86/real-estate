from typing import List

from realty.domain.flat.entities import FlatEntity
from realty.domain.floor.entities import FloorEntity
from realty.repositories.floor import FloorRepository


class FloorSelector:
    @staticmethod
    def get_floors_with_total_flats() -> List[FlatEntity]:
        return FloorRepository.fetch_all_floors()

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
        flats, floor = FloorRepository.fetch_floor_detail(pk)
        data = FloorSelector.query_set_to_dataclass(flats, floor)

        return data
