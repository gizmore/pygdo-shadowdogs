from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException
from gdo.shadowdogs.locations.Location import Location


class Exit(Location):

    def sd_methods(self) -> list[str]:
        return [
            'sdleave',
        ]

    def sd_exit_to(self) -> Location:
        raise ShadowdogsException('err_sd_stub')
