from dataclasses import dataclass

from realty.domain.flat.entities import FlatEntity


@dataclass
class SectionEntity:
    id: int
    name: str
    number: int
    flats: list[FlatEntity]