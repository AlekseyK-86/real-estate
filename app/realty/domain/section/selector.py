from typing import List

from realty.domain.flat.entities import FlatEntity
from realty.domain.section.entities import SectionEntity
from realty.repositories.section import SectionRepository


class SectionSelector:
    @staticmethod
    def get_sections_with_total_flats() -> List[FlatEntity]:
        return SectionRepository.fetch_all_sections()

    @staticmethod
    def query_set_to_dataclass(queryset, section) -> List[FlatEntity]:
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
    def get_section_detail(pk) -> List[FlatEntity]:
        flats, floor = SectionRepository.fetch_section_detail(pk)   
        data = SectionSelector.query_set_to_dataclass(flats, floor)

        return data
