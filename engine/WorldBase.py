from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.locations.City import City


class WorldBase(WithShadowFunc):

    CITIES: dict[str,City] = {
    }

    def __repr__(self):
        return self.__class__.__name__
