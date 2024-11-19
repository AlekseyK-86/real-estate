from typing import List

from realty.domain.project.entities import ProjectEntity
from realty.repositories.project import ProjectRepository

class ProjectSelector:
    @staticmethod
    def get_all_projects() -> List[ProjectEntity]:
        return ProjectRepository.fetch_all_projects()

    @staticmethod
    def get_project_detail(pk) -> List[ProjectEntity]:
        return ProjectRepository.fetch_project_detail(pk)
