from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.Query import Query
from gdo.base.Render import Mode, Render
from gdo.shadowdogs.GDT_City import GDT_City
from gdo.shadowdogs.SD_Place import SD_Place
from gdo.shadowdogs.WithShadowMethod import WithShadowMethod
from gdo.table.MethodQueryTable import MethodQueryTable


class places(WithShadowMethod, MethodQueryTable):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdplaces'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdpl'

    def gdo_parameters(self) -> list[GDT]:
        return [
            GDT_City('city').default_current().not_null(),
        ]

    def gdo_table(self) -> GDO:
        return SD_Place.table()

    def gdo_table_query(self) -> Query:
        loc = self.parameter('city').player(self.get_player()).get_city().get_location_key()
        return (SD_Place.table().select().where('kp_player='+self.get_player().get_id()).
                join_object('kp_location').where(f'l_name LIKE "{loc}%"'))

    def render_gdo(self, gdo: GDO, mode: Mode) -> any:
        self._curr_table_row_id += 1
        return f"{Render.bold(str(self._curr_table_row_id), mode)}-{gdo.get_location().render_name()}"
