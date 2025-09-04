from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.base.Render import Render
from gdo.base.Trans import t
from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.WithShadowMethod import WithShadowMethod


class equipment(WithShadowMethod, Method):

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdq'

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdequipment'

    """
    Display your equipment.
    """
    def gdo_execute(self) -> GDT:
        pl = self.get_player()
        display = []
        for slot in GDT_Slot.SLOTS:
            if item := pl.get_equipment(slot):
                item_name = Render.bold(item.render_name(), self._env_mode)
            else:
                continue
                # item_name = Render.italic(t('none'), self._env_mode)
            display.append(GDT_Slot.display_slot(slot) + ': ' + item_name)
        if not display:
            display.append(Render.italic(t('none'), self._env_mode))
        return self.msg('msg_sd_equipment', ("; ".join(display),))
