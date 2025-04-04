from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException
from gdo.shadowdogs.locations.Location import Location


class City:

    LOCATIONS: list[Location] = []

    def coordinates(self) -> (float, float, float, float):
        pass

    def get_location(self, loc_str: str):
        matches = []
        for location in self.LOCATIONS:
            if loc_str in location.get_name():
                matches.append(location)
        if len(matches) == 0:
            raise ShadowdogsException('err_sd_no_match')
        if len(matches) == 1:
            return matches[0]
        raise ShadowdogsException('err_sd_much_matches')

    def get_name(self):
        return self.__class__.__name__
