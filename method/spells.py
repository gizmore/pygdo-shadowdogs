from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.shadowdogs.GDT_City import GDT_City
from gdo.shadowdogs.engine.MethodSD import MethodSD


class spells(MethodSD):

    def gdo_trigger(self) -> str:
        return 'sdspells'

    def gdo_parameters(self) -> [GDT]:
        return [
        ]

    def gdo_execute(self) -> GDT:
        return self.empty()