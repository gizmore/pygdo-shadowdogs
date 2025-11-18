from gdo.base.Trans import t
from gdo.shadowdogs.attr.Attribute import Attribute
from gdo.shadowdogs.engine.MethodSD import MethodSD


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
            attrs.append("%s: %d(%d)" % (t(key)[:3], player.gb(key), player.g(key)))
        return self.reply('msg_sd_attributes', (", ".join(attrs),))
