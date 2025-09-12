from gdo.message.GDT_HTML import GDT_HTML
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Bed(Obstacle):

    def sd_commands(self) -> list[str]:
        return [
            'sdsleep',
        ]

    async def on_sleep(self):
        party = self.get_party()
        await self.send_to_party(party, 'msg_sd_bedtime')
        await party.do(Action.SLEEP)
        return GDT_HTML()
