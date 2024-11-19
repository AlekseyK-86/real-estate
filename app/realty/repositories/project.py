from typing import List

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Count, Prefetch

from realty.domain.project.entities import ProjectEntity
from realty.models.building import Building
from realty.models.project import Project

class ProjectRepository:
    @staticmethod
    def fetch_all_projects() -> List[ProjectEntity]:        
        return Project.objects.all()

    @staticmethod
    def fetch_project_detail(pk) -> List[ProjectEntity]:
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
        
        return project