from gdo.base.Trans import t
from gdo.core.GDT_String import GDT_String
from gdo.shadowdogs.attr.Attribute import Attribute
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class attributes(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return "sdattributes"

    @classmethod
    def gdo_trig(cls) -> str:
        return "sdat"

    async def sd_execute(self):
        attrs = []
        player = self.get_player()
        for key in Attribute.ATTRIBUTES:
            attrs.append("%s: %d(%d)" % (t(key), player.gb(key), player.g(key)))
        return GDT_String('attributes').val(t('msg_sd_attributes', (", ".join(attrs),)))
