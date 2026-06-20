from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.city.y2064.Nauen.locations.paulinaue.LoveTake2 import LoveTake2
from gdo.shadowdogs.city.y2064.Peine.locations.thomann.TBS import TBS
from gdo.shadowdogs.obstacle.Obstacle import Obstacle

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player

class Computer(Obstacle):

    async def on_use(self, target: 'SD_Player|Obstacle'):
        q1 = LoveTake2.instance()
        q2 = TBS.instance()
        if not q1.is_done() and not q2.is_in_quest():
            await self.on_q1(q1)
        elif q1.is_done() and not q2.is_done():
            await self.on_q2(q2)

    async def on_q1(self, q: TBS):
        times = int(q.qv_get('times', '0')) + 1
        q.qv_set('times', str(times))
        await self.send_to_player(self.get_player(), 'sdqc_love2')
        if times > 8:
            await q.accept()

    async def on_q2(self, q: TBS):
        await self.get_party().do(Action.WORK)
        await self.send_to_player(self.get_player(), 'sdqc_tbs')



