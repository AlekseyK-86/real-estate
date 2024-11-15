from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Count, Prefetch

from realty.domain.building.entities import BuildingEntity
from realty.domain.project.entities import ProjectEntity
from realty.models.building import Building
from realty.models.project import Project
from typing import List


class ProjectSelector:
    @staticmethod
    def get_all_projects() -> List[ProjectEntity]:
        projects = Project.objects.all()
        return projects

    @staticmethod
    def get_project_detail(pk) -> List[ProjectEntity]:
        try:
            project = (
                Project.objects.prefetch_related(
                    Prefetch('building_set',
                             queryset=Building.objects.annotate(total_flats=Count('flat')))
                )
                .get(id=pk)
            )
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist(f"Объект c id={pk} в модели Project не найден.")
        except MultipleObjectsReturned:
            raise MultipleObjectsReturned(f"Что то пошло не так, из модели Project вернулось более чем один объект.")
        data = ProjectEntity(
            id=project.id,
            name=project.name,
            description=project.description,
            buildings=[
                BuildingEntity(
                    id=building.id,
                    floors=building.floors,
                    name=building.name,
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
