from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_Spell import GDT_Spell
from gdo.shadowdogs.GDT_TargetArg import GDT_TargetArg
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.spells.Spell import Spell


class cast(MethodSD):

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdc'

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdcast'

    def sd_combat_seconds(self) -> int:
        return self.get_spell().sd_cast_time(self.get_player())

    def sd_method_is_instant(self) -> bool:
        return False

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_fields(
            GDT_Spell('spell').not_null(),
            GDT_TargetArg('target').friends().foes().others().obstacles().positional(),
        )
        super().gdo_create_form(form)

    def get_spell(self) -> Spell:
        return self.param_value('spell')

    def get_target(self) -> SD_Player:
        return self.param_value('target')

    async def sd_execute(self):
        await self.get_spell().cast(self.get_player(), self.get_target())
