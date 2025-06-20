from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.shadowdogs.WithShadowMethod import WithShadowMethod


class look(WithShadowMethod, Method):

    def gdo_parameters(self) -> list[GDT]:
        return [

        ]

    def gdo_execute(self) -> GDT:
        pass
