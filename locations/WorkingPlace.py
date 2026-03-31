from gdo.shadowdogs.locations.Location import Location


class WorkingPlace(Location):

    def sd_methods(self) -> list[str]:
        return [
            'sdwork',
        ]
