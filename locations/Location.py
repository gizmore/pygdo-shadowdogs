from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.obstacle.Obstacle import Obstacle

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.locations.City import City


class Location(WithShadowFunc):

    OBSTACLES: list[Obstacle] = [

    ]

    def sd_methods(self) -> list[str]:
        return []

    def get_city(self) -> 'City':
        pass

    def get_location_key(self) -> str:
        m = self.__class__.__module__.split('.')
        return m[3] + "." + m[5]

