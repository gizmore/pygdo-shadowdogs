from typing import TYPE_CHECKING

from gdo.base.Trans import t
from gdo.date.Time import Time
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party


class Action(WithShadowFunc):

    EXPLORE = 'explore'
    FIGHT = 'fight'
    GOTO = 'goto'
    HACK = 'hack'
    INSIDE = 'inside'
    OUTSIDE = 'outside'
    SLEEP = 'sleep'
    TALK = 'talk'
    TRAVEL = 'travel'
    WORK = 'work'

    def get_target(self, party: 'SD_Party', target_string: str):
        raise ShadowdogsException('err_sd_stub', (f'{self.get_name()}.get_target()',))

    async def on_start(self, party: 'SD_Party'):
        raise ShadowdogsException('err_sd_stub', (f'{self.get_name()}.on_start()',))

    async def execute(self, party: 'SD_Party'):
        raise ShadowdogsException('err_sd_stub', (f'{self.get_name()}.execute()',))

    async def sleeping(self, party: 'SD_Party'):
        pass

    async def on_completed(self, party: 'SD_Party'):
        for member in party.members:
            await member.combat_tick()

    ##########
    # Render #
    ##########

    def get_name(self) -> str:
        return self.__class__.__name__

    def __repr__(self):
        return f"Action:{self.get_name()}"

    def render_name(self) -> str:
        return t(self.__class__.__name__)

    def get_action_text_key(self, party: 'SD_Party', scope: str = 'start') -> str:
        return f"msg_sd_{scope}_{self.get_name()}"

    def get_action_text_args(self, party: 'SD_Party', scope: str = 'start') -> None|tuple[any,...]:
        if party.get_eta_s():
            return party.render_members(), self.get_target(party, party.get_target_string()).get_name(), self.render_busy(party)
        return party.render_members(), self.get_target(party, party.get_target_string()).render_name()

    def render_busy(self, party: 'SD_Party') -> str:
        return Time.human_duration(party.get_eta_s())

    def render_action(self, party: 'SD_Party', scope: str = 'start') -> str:
        return t(self.get_action_text_key(party, scope), self.get_action_text_args(party, scope))
