from gdo.date.Time import Time
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.city.y2064.Brunswick.locations.school.Computers import Computers
from gdo.shadowdogs.city.y2064.Brunswick.locations.school.HeyTaxi import HeyTaxi
from gdo.shadowdogs.city.y2064.Nauen.locations.paulinaue.LoveTake2 import LoveTake2
from gdo.shadowdogs.city.y2064.Peine.locations.thomann.TBS import TBS
from gdo.shadowdogs.obstacle.Obstacle import Obstacle

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player

class Computer(Obstacle):

    def sd_commands(self) -> list[str]:
        return [
            'sduse',
        ]

    def sd_can_use_on_self(self) -> bool:
        return True

    async def on_use(self, target: 'SD_Player|Obstacle'):
        q1 = Computers.instance()
        q2 = TBS.instance()
        q3 = HeyTaxi.instance()
        q4 = LoveTake2.instance()
        if not q1.is_done():
            await self.on_q1(q1)
        elif not q2.is_done():
            await self.on_q2(q2)
        elif not q3.is_done():
            await self.on_q3(q3)
        elif not q4.is_accepted():
            await self.on_q4(q4)
        else:
            await self.send_to_player(self.get_player(), 'sdq_home_computer')

    async def on_q1(self, q: Computers):
        if not q.is_accepted(self.get_player()):
            await self.send_to_player(self.get_player(), 'sdqc_computers')
            await q.accept()
        else:
            await self.send_to_player(self.get_player(), 'sdqc_computers2')

    async def on_q2(self, q: TBS):
        if not q.is_accepted(self.get_player()):
            await self.send_to_player(self.get_player(), 'sdqc_tbs1')
            await q.accept()
        else:
            await self.get_party().do(Action.WORK, self.fqcn(), q.WORK_TIME)
            await self.send_to_player(self.get_player(), 'sdqc_tbs2')

    async def on_q3(self, q: HeyTaxi):
        if not q.is_accepted(self.get_player()):
            await self.send_to_player(self.get_player(), 'sdqc_tbs1')
            await q.accept()
            await self.send_to_player(self.get_player(), 'sdqc_tbs2', (Time.human_duration(q.QUEST_TIME)))

        else:
            await self.get_party().do(Action.WORK, self.fqcn(), q.WORK_TIME)
            await self.send_to_player(self.get_player(), 'sdqc_tbs2')

    async def on_q4(self, q: LoveTake2):
        times = int(q.qv_get('times', '0')) + 1
        q.qv_set('times', str(times))
        await self.send_to_player(self.get_player(), 'sdqc_love1_' + str(times))
        if times > 8:
            await q.accept()

    async def on_work_over(self):
        q2 = TBS.instance()
        if q2.is_in_quest():
            times = int(q2.qv_get('times', '0')) + 1
            q2.qv_set('times', str(times))
            if times >= TBS.WORK_TIMES:
                await q2.accomplished()
