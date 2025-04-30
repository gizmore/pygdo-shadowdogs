from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg


class examine(Method):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdexamine'

    def gdo_parameters(self) -> list[GDT]:
        return [
            GDT_ItemArg('item').inventory().equipment(),
        ]

    def gdo_execute(self) -> GDT:
        pass
