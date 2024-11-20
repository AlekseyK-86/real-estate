from typing import List

from realty.domain.flat.entities import FlatEntity
from realty.repositories.section import SectionRepository


class SectionSelector:

    @staticmethod
    def get_sections_with_total_flats() -> List[FlatEntity]:
        return SectionRepository.fetch_all_sections()

    @staticmethod
    def get_section_detail(pk) -> List[FlatEntity]:
        return SectionRepository.fetch_section_detail(pk)
