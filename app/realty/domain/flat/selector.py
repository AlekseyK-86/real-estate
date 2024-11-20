from typing import List

from realty.domain.flat.entities import FlatEntity
from realty.repositories.flat import FlatRepository

from drf_spectacular.utils import extend_schema


class FlatSelector:

    @staticmethod
    #@extend_schema(summary="API для получение всех квартир ")
    def get_all_flats():
        return FlatRepository.fetch_all_flats()      

    @staticmethod
    #@extend_schema(summary="API для получение одной квартир ")
    def get_flat_by_id(pk) -> List[FlatEntity]:
        return FlatRepository.fetch_flat_detail(pk)
