from gdo.date.Time import Time
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.city.y2064.Peine.locations.seniorhome.Nurse import Nurse
from gdo.shadowdogs.city.y2064.Peine.locations.seniorhome.CivilService import CivilService
from gdo.shadowdogs.locations.Location import Location

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class SeniorHome(Location):

    NPCS: list['type[TalkingNPC]'] = [
        Nurse,
    ]

    def sd_methods(self) -> list[str]:
        return [
            'sdwork',
        ]

    async def on_entered(self):
        for player in self.get_party().members:
            if not CivilService.instance().is_accepted(player):
                await self.send_to_party(self.get_party(), 'msg_sd_senior_home_quest')
                await self.get_party().do(Action.OUTSIDE)
                return self
        return await super().on_entered()

    async def on_work(self):
        if CivilService.instance().is_in_quest():
            await self.get_party().do(Action.WORK, self.get_location_key(), Time.ONE_HOUR)
            await self.send_to_party(self.get_party(), 'sdqs_working')
        else:
            await self.send_to_party(self.get_party(), 'sdqs_no_work_here')

    async def on_work_over(self):
        await CivilService.instance().on_worked()
