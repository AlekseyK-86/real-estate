from dataclasses import dataclass

from realty.domain.floor.entities import FloorEntity


@dataclass
class SectionEntity:
    id: int
    name: str
    number: int

@dataclass
class DetailSectionEntity(SectionEntity):
    total_flats: int