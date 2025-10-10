from gdo.base.GDT import GDT
from gdo.base.Trans import t
from gdo.core.GDT_String import GDT_String
from gdo.date.Time import Time
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
        busytimes = []
        for player in party.members:
            if busytime := player.get_busy_seconds():
                busytimes.append(self.t('sd_party_busytime', (player.render_name(), Time.human_duration(busytime))))
        return self.reply('msg_sd_party_info', (action.render_action(party, 'party'), ", ".join(busytimes)))
