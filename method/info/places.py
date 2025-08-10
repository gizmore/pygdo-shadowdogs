from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.base.Result import Result
from gdo.base.ResultArray import ResultArray
from gdo.shadowdogs.GDT_City import GDT_City
from gdo.shadowdogs.SD_Place import SD_Place
from gdo.shadowdogs.WithShadowMethod import WithShadowMethod
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.table.MethodTable import MethodTable


class places(WithShadowMethod, MethodTable):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdplaces'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdpl'

    def gdo_parameters(self) -> list[GDT]:
        return [
            GDT_City('City').default_current().not_null(),
        ]

    def gdo_table_result(self) -> Result:
        p = self.get_player()
        SD_Place.table().select().where('sp')
        return ResultArray(self.get_player().inventory, SD_Place.table())
