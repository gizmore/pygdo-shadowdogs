from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.shadowdogs.GDT_City import GDT_City


class known_places(Method):
    def gdo_trigger(self) -> str:
        return 'sdknown_places'

    def gdo_parameters(self) -> [GDT]:
        return [
            GDT_City('City').default_current().not_null(),
        ]

    def gdo_execute(self) -> GDT:
        return self.empty()
