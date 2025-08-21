from gdo.base.Util import html
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.GDT_Word import GDT_Word
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.MethodSD import MethodSD


class say(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return "sdsay"

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_Player('to').nearby().npcs().not_null(),
            GDT_Word('word').not_null(),
        )
        super().gdo_create_form(form)

    def get_target(self) -> SD_Player:
        return self.param_value('to')

    async def sd_execute(self):
        for player in self.nearby_players(self.get_player()):
            await self.send_to_player(player, 'msg_sd_say', (self.get_player().render_name(), html(self.param_value('word'))))
        await self.get_target().on_say(self.get_player(), self.param_value('word'))
