from functools import partial

from gdo.base.Application import Application
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodSD import MethodSD


class exit(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdexit'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdx'

    def sd_requires_action(self) -> list[str] | None:
        return [Action.INSIDE]

    def sd_is_leader_command(self) -> bool:
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
        await party.get_target().on_exited()
