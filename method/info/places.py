from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.base.Query import Query
from gdo.base.Render import Mode, Render
from gdo.base.Trans import t
from gdo.shadowdogs.GDT_City import GDT_City
from gdo.shadowdogs.SD_Place import SD_Place
from gdo.shadowdogs.WithShadowMethod import WithShadowMethod
from gdo.table.MethodQueryTable import MethodQueryTable

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.locations.City import City


class places(WithShadowMethod, MethodQueryTable):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdplaces'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdkp'

    def gdo_paginated(self) -> bool:
        return False

    def gdo_parameters(self) -> list[GDT]:
        return [
            GDT_City('city').default_current().not_null(),
        ]

    def gdo_render_title(self) -> str:
        return t('mt_shadowdogs_places', (self.get_num_results(), self.get_city().render_name()))

    def get_city(self) -> 'City':
        return self.parameter('city').player(self.get_player()).get_city()

    def gdo_table(self) -> GDO:
        return SD_Place.table()

    def gdo_table_query(self) -> Query:
        loc = self.get_city().get_location_key()
        return (SD_Place.table().select().where('kp_player='+self.get_player().get_id()).
                join_object('kp_location').where(f'l_name LIKE "{loc}%"'))

    def render_gdo(self, gdo: GDO, mode: Mode) -> any:
        self._curr_table_row_id += 1
        return f"{Render.bold(str(self._curr_table_row_id), mode)}-{gdo.get_location().render_name()}"
