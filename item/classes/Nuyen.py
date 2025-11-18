from gdo.base.Trans import t
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.item.Item import Item


class Nuyen(Item):

    def render_name(self) -> str:
        return Shadowdogs.display_nuyen(self.get_count())

    def render_name_wc(self) -> str:
        return t(self.get_item_name())
