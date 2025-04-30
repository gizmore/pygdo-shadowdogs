from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.MethodSD import MethodSD


class view(MethodSD):

    def sd_is_location_specific(self) -> bool:
        return True


    def gdo_parameters(self) -> list[GDT]:
        return [
        ]

    def gdo_execute(self) -> GDT:
        pass

