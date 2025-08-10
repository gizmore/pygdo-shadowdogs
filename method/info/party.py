from gdo.base.GDT import GDT
from gdo.base.Trans import t
from gdo.core.GDT_String import GDT_String
from gdo.shadowdogs.engine.MethodSD import MethodSD


class party(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdparty'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdp'

    async def sd_execute(self) -> GDT:
        party = self.get_party()
        action = party.get_action()
        return GDT_String('info').val(action.render_action(party, 'party'))
