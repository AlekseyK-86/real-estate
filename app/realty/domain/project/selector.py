from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Count, Prefetch

from realty.domain.building.entities import BuildingEntity
from realty.domain.project.entities import ProjectEntity
from realty.models.building import Building
from realty.models.project import Project


class ProjectSelector:
    pass
