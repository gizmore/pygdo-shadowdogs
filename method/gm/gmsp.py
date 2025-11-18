from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.GDT_Spell import GDT_Spell
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.spells.Spell import Spell


class gmsp(MethodSD):

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_fields(
            GDT_Player('to').humans().not_null(),
            GDT_Spell('spell').not_null(),
        )
        super().gdo_create_form(form)

    def get_target(self) -> SD_Player:
        return self.param_value('to')

    def get_spell(self) -> Spell:
        return self.param_value('spell')

    async def sd_execute(self):
        to = self.get_target()
        spell = self.get_spell()
        await self.give_spell(to, spell)
        return self.reply('msg_sd_gmsp', (spell.render_name(),))
