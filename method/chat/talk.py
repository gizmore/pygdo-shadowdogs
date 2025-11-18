from gdo.base.Util import html
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.GDT_Word import GDT_Word
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.MethodSD import MethodSD


class talk(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return "sdtalk"

    @classmethod
    def gdo_trig(cls) -> str:
        return "sdt"

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_fields(
            GDT_Player('to').nearby().npcs().humans().not_null(),
            GDT_Word('word').not_null(),
        )
        super().gdo_create_form(form)

    def get_target(self) -> SD_Player:
        return self.param_value('to')

    async def sd_execute(self):
        p = self.get_player()
        t = self.get_target()
        await t.player(p).on_say(p, self.param_value('word'))
        return self.empty()
