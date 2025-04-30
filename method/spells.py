from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.shadowdogs.GDT_City import GDT_City
from gdo.shadowdogs.engine.MethodSD import MethodSD


class spells(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdspells'

    def gdo_parameters(self) -> list[GDT]:
        return [
        ]

    def gdo_execute(self) -> GDT:
        return self.empty()