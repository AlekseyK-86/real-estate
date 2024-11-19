from typing import List

from realty.domain.building.entities import BuildingDetailEntity, BuildingEntity
from realty.repositories.building import BuildingRepository


class BuildingSelector:
    @staticmethod
    def get_all_buildings() -> List[BuildingEntity]:
        return BuildingRepository.fetch_all_buildings()

    @staticmethod
    def get_building_detail(pk) -> List[BuildingDetailEntity]:
        return BuildingRepository.fetch_building_detail(pk)
