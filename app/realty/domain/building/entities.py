from dataclasses import dataclass


@dataclass
class BuildingEntity:
    id: int
    floors: int
    name: str
    photo: str
    date_of_construction: str
    date_of_delivery: str
    address: str
    number: int
    status: str
    type: str
    has_parking: bool
    elevators: int
    project_name: str
    #total_flats: int


@dataclass
class BuildingDetailEntity(BuildingEntity):
    total_flats: int
