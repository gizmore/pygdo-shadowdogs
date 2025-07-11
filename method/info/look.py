from gdo.base.Util import Arrays
from gdo.language.GDT_Trans import GDT_Trans
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodSD import MethodSD


class look(MethodSD):

    def sd_requires_action(self) -> list[str] | None:
        return [
            Action.INSIDE,
            Action.OUTSIDE,
        ]

    async def sd_execute(self):
        objs = []
        location = self.get_location()
        party = self.get_party()
        for obstacle in location.obstacles(party.get_action_name(), self.get_player()):
            objs.append(obstacle.render_name())
        for player in party.other_players():
            objs.append(player.render_name())
        return GDT_Trans().text('msg_sd_look', (Arrays.human_join(objs),))

