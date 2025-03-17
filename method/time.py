from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.date.Time import Time
from gdo.date.GDT_DateTime import GDT_DateTime
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class time(WithShadowFunc, Method):
    def gdo_trigger(self) -> str:
        return 'sdtime'

    def gdo_execute(self) -> GDT:
        return GDT_DateTime('shadowtime').val(Time.get_date(Shadowdogs.get_time()))
