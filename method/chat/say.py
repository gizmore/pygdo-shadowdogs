from gdo.base.Util import html
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_Word import GDT_Word
from gdo.shadowdogs.engine.MethodSD import MethodSD


class say(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return "sdsay"

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_Word('words').not_null(),
        )
        super().gdo_create_form(form)

    async def sd_execute(self):
        p = self.get_player()
        text = self.param_value('words')
        for player in p.nearby_players(p):
            await self.send_to_player(player,'msg_sd_say', (p.render_name(), html(text)))
        return self.empty()
