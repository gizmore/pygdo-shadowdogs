from gdo.base.GDT import GDT
from gdo.base.Trans import t
from gdo.core.GDT_String import GDT_String
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.engine.MethodSD import MethodSD


class examine(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdexamine'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdex'

    def gdo_parameters(self) -> list[GDT]:
        return [
            GDT_ItemArg('item').inventory().equipment().not_null(),
        ]

    def get_item(self) -> SD_Item:
        return self.param_value('item')

    def gdo_execute(self) -> GDT:
        item = self.get_item()
        mods = {t(k): v for k, v in item.all_player_modifiers() if v != 0}
        return GDT_String('examined').val(t('msg_sd_examine', (item.render_name(), f"{mods}")))
