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

    def get_target(self, party: 'SD_Party', target_string: str):
        raise ShadowdogsException('err_sd_stub', (f'{self.get_name()}.get_target()',))

    async def on_start(self, party: 'SD_Party'):
        raise ShadowdogsException('err_sd_stub', (f'{self.get_name()}.on_start()',))

    async def execute(self, party: 'SD_Party'):
        pass

    async def sleeping(self, party: 'SD_Party'):
        pass

    async def on_completed(self, party: 'SD_Party'):
        pass

    ##########
    # Render #
    ##########

    def get_name(self) -> str:
        return self.__class__.__name__

    def get_action_text_key(self, party: 'SD_Party', scope: str = 'start') -> str:
        return f"sd_action_{scope}_{self.get_name()}"

    def get_action_text_args(self, party: 'SD_Party', scope: str = 'start') -> tuple[str,...]:
        if scope == 'start':
            if party.get_eta_s():
                return party.render_members(), self.get_target(party).render_name(), self.render_busy(party)
            return party.render_members(), self.get_target(party).render_name()

    def render_busy(self, party: 'SD_Party') -> str:
        return Time.human_duration(party.get_eta_s())

    def render_action(self, party: 'SD_Party', scope: str = 'start') -> str:
        return t(self.get_action_text_key(party, ''), self.get_action_text_args(party, 'party'))
