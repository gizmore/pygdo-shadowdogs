from gdo.base.GDT import GDT
from gdo.base.Trans import t
from gdo.core.GDT_String import GDT_String
from gdo.shadowdogs.engine.MethodSD import MethodSD


class party(MethodSD):

    def gdo_execute(self) -> GDT:
        p = self.get_party()

        return GDT_String('info').val(t('msg_sd_party', ()))

