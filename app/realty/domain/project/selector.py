from typing import List

from realty.domain.building.entities import BuildingEntity
from realty.domain.project.entities import ProjectEntity
from realty.repositories.project import ProjectRepository

class ProjectSelector:
    @staticmethod
    def get_all_projects() -> List[ProjectEntity]:
        return ProjectRepository.fetch_all_projects()

    @staticmethod
    def get_project_detail(pk) -> List[ProjectEntity]:
        project = ProjectRepository.fetch_project_detail(pk)
        
        data = ProjectEntity(
            id=project.id,
            name=project.name,
            description=project.description,
            photo=project.photo,
            buildings=[
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
                for building in project.building_set.all()
            ]
        )

        return data
