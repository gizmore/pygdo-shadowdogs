from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.engine.MethodSD import MethodSD


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class attack(MethodSD):

    @classmethod
    def sd_trig(cls) -> str:
        return "sda"

    def sd_requires_action(self) -> list[str]|None:
        return [
            'fight',
        ]

    def sd_combat_seconds(self) -> float:
        return self.get_player().get_weapon().get_attack_time()

    def gdo_create_form(self, form: GDT_Form) -> None:
        from gdo.shadowdogs.GDT_TargetArg import GDT_TargetArg
        form.add_field(GDT_TargetArg('target').foes().not_null())
        super().gdo_create_form(form)

    def get_target(self) -> 'SD_Player':
        return self.param_value('target')

    def sd_execute(self):
        self.get_player().get_weapon().attack(self.get_target())
        return self.empty()
