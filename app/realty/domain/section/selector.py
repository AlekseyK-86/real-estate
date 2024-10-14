from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from realty.domain.floor.entities import FloorEntity
from realty.domain.section.entities import SectionEntity, DetailSectionEntity
from realty.models.floor import Floor
from realty.models.section import Section


class SectionSelector:
    @staticmethod
    def get_all_sections():
        sections = Section.objects.all()
        return sections

    @staticmethod
    def get_section_detail(pk):
        try:
            section = Section.objects.prefetch_related(
                'flat_set__floor'
            ).get(id=pk)
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            return None

        data = SectionEntity(
            id=section.id,
            name=section.name,
            number=section.number,
        )

        return data
