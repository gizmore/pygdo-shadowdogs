from gdo.base.GDT import GDT
from gdo.base.Method import Method


class goto(Method):
    def gdo_parameters(self) -> [GDT]:
        return [
            GDT_Location('to').known().not_null(),
        ]

    def gdo_execute(self) -> GDT:
        pass
    