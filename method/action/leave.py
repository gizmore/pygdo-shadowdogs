from functools import partial

from gdo.base.Application import Application
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodSD import MethodSD


class leave(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdleave'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdle'

    def sd_location_actions(self) -> tuple[str]:
        return (Action.INSIDE,)

    def sd_is_leader_command(self) -> bool:
        return True

    def sd_is_location_specific(self) -> bool:
        return True

    def sd_combat_seconds(self) -> int:
        return self.get_location().sd_entrance_seconds()

    async def sd_execute(self):
        time = self.sd_combat_seconds()
        self.get_party().all_busy(time)
        Application.EVENTS.add_timer_async(time, partial(self.on_leave))
        await self.send_to_party(self.get_party(), 'msg_sd_leaving', (self.get_location().render_name(),))
        return self.empty()

    async def on_leave(self):
        party = self.get_party()
        await party.do(Action.OUTSIDE)
