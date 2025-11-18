from gdo.base.Application import Application
from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.date.Time import Time
from gdo.date.GDT_DateTime import GDT_DateTime
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class time(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdtime'

    def sd_requires_player(self) -> bool:
        return False

    def gdo_execute(self) -> GDT:
        return GDT_DateTime('shadowtime').val(Time.get_date(Application.TIME + Time.ONE_YEAR * 64))

