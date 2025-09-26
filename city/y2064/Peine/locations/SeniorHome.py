from gdo.date.Time import Time
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.city.y2064.Peine.npcs.Nurse import Nurse
from gdo.shadowdogs.city.y2064.Peine.quests.CivilService import CivilService
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

    async def on_work(self):
        await self.get_party().do(Action.WORK, self.get_location_key(), Time.ONE_HOUR)

    async def on_work_over(self):
        await CivilService.instance().on_worked()
        await self.get_party().do(Action.WORK, self.get_location_key(), Time.ONE_HOUR)
