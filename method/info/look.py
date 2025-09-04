from gdo.base.Util import Arrays
from gdo.language.GDT_Trans import GDT_Trans
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodSD import MethodSD


class look(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdlook'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdl'

    def sd_requires_action(self) -> list[str] | None:
        return [
            Action.INSIDE,
            Action.OUTSIDE,
        ]

    async def sd_execute(self):
        players = []
        for player in self.nearby_players(self.get_player()):
            players.append(player.render_name())
        return self.reply('msg_sd_look', (Arrays.human_join(players),))
