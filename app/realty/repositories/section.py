from typing import List

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Count

from realty.domain.project.entities import ProjectEntity
from realty.models.section import Section

class SectionRepository:
    @staticmethod
    def fetch_all_sections() -> List[ProjectEntity]:
        return Section.objects.annotate(total_flats=Count('flat'))

    @staticmethod
    def fetch_section_detail(pk) -> List[ProjectEntity]:
        try:
            floor = Section.objects.prefetch_related(
                'flat_set__floor',
                'flat_set__category',
                'flat_set__building'
            ).get(id=pk)

        except ObjectDoesNotExist:
            raise ObjectDoesNotExist(f"Объект c id={pk} в модели Section не найден.")

        except MultipleObjectsReturned:
            raise MultipleObjectsReturned(f"Что то пошло не так, из модели Section вернулось более чем один объект.")

        flats = floor.flat_set.all()

        return (flats, floor)