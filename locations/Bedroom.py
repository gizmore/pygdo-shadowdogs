from gdo.shadowdogs.locations.Location import Location


class Bedroom(Location):

    def sd_methods(self) -> list[str]:
        return [
            'sdsearch',
            'sdsleep',
        ]
