from gdo.base.Util import Arrays
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodSD import MethodSD


class info(MethodSD):

    def sd_requires_action(self) -> list[str] | None:
        return [Action.INSIDE, Action.OUTSIDE]

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdinfo'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdin'

    async def sd_execute(self):
        pl = self.get_player()
        loc = self.get_location()
        obs = [o.render_name() for o in loc.obstacles(pl.get_action_name(), pl)] or [self.t('nothing')]
        return self.reply('msg_sd_info', (loc.render_name(), loc.render_descr(pl), Arrays.human_join(obs) ))

