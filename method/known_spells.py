from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.shadowdogs.GDT_City import GDT_City


class known_spells(Method):

    def gdo_trigger(self) -> str:
        return 'sdknown_spells'

    def gdo_parameters(self) -> [GDT]:
        return [
        ]

    def gdo_execute(self) -> GDT:
        return self.empty()