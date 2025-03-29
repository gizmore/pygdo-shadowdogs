from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc


class sell(WithShadowFunc, Method):

    def gdo_parameters(self) -> [GDT]:
        return [
            GDT_ItemArg('item').inventory().not_null(),
        ]

    def gdo_execute(self) -> GDT:
        pass
