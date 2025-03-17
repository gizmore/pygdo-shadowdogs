from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.shadowdogs.GDT_City import GDT_City


class known_places(Method):
    def gdo_parameters(self) -> [GDT]:
        return [
            GDT_City('City').default_current(),
        ]

    def gdo_execute(self) -> GDT:
        return self.empty()