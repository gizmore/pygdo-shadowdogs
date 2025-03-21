from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg


class examine(Method):

    def gdo_trigger(self) -> str:
        return 'sdexamine'

    def gdo_parameters(self) -> [GDT]:
        return [
            GDT_ItemArg('item').inventory().equipment(),
        ]

    def gdo_execute(self) -> GDT:
        pass
