from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.city.y2064.Peine.Peine import Peine
from gdo.shadowdogs.locations.City import City


class World2064(WithShadowFunc):

    Peine: Peine = Peine()

    CITIES: dict[str,City] = {
        'Peine': Peine,
    }
