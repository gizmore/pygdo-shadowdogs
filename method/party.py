from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.core.GDT_String import GDT_String
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc


class party(WithShadowFunc, Method):

    def gdo_execute(self) -> GDT:


        return GDT_String('info').val()
