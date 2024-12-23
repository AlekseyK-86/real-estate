from typing import List

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Count

from realty.domain.flat.entities import FlatEntity
from realty.domain.section.entities import SectionEntity
from realty.models.section import Section

class SectionRepository:

    @staticmethod
    def fetch_all_sections() -> List[SectionEntity]:
        section = Section.objects.annotate(total_flats=Count('flat'))

        return section

    @staticmethod
    def query_set_to_dataclass(queryset, section) -> SectionEntity:
        return SectionEntity(
            id=section.id,
            name=section.name,
            number=section.number,
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
    def fetch_section_detail(pk) -> SectionEntity:
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
        data = SectionRepository.query_set_to_dataclass(flats, floor)

        return data
