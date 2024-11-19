from typing import List

from realty.domain.building.entities import BuildingDetailEntity, BuildingEntity
from realty.repositories.building import BuildingRepository


class BuildingSelector:
    @staticmethod
    def get_all_buildings() -> List[BuildingEntity]:
        buildings = BuildingRepository.fetch_all_buildings()
        data = [
            BuildingEntity(
                id=building.id,
                floors=building.floors,
                name=building.name,
                photo=building.photo,
                date_of_construction=building.date_of_construction,
                date_of_delivery=building.date_of_delivery,
                address=building.address,
                number=building.number,
                status=building.status,
                type=building.type,
                has_parking=building.has_parking,
                elevators=building.elevators,
                project_name=building.project.name
            )
            for building in buildings
        ]
        
        return data

    @staticmethod
    def get_building_detail(pk) -> List[BuildingDetailEntity]:
        building, total_flats = BuildingRepository.fetch_building_detail(pk)

        data = BuildingDetailEntity(
            id=building.id,
            floors=building.floors,
            name=building.name,
            photo=building.photo,
            date_of_construction=building.date_of_construction,
            date_of_delivery=building.date_of_delivery,
            address=building.address,
            number=building.number,
            status=building.status,
            type=building.type,
            has_parking=building.has_parking,
            elevators=building.elevators,
            project_name=building.project.name,
            total_flats=total_flats
        )

        return data
