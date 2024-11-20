from typing import List

from realty.domain.flat.entities import FlatEntity
from realty.domain.floor.entities import FloorEntity
from realty.repositories.floor import FloorRepository


class FloorSelector:
    @staticmethod
    def get_floors_with_total_flats() -> List[FloorEntity]:
        return FloorRepository.fetch_all_floors()

    @staticmethod
    def get_floor_detail(pk) -> List[FlatEntity]:
        data = FloorRepository.fetch_floor_detail(pk)

        return data
