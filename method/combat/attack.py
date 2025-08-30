from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.engine.MethodSD import MethodSD


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class attack(MethodSD):

    @classmethod
    def sd_trigger(cls) -> str:
        return "sdattack"

    @classmethod
    def sd_trig(cls) -> str:
        return "sda"

    def sd_is_item_specific(self) -> bool:
        return True

    def sd_requires_action(self) -> list[str]|None:
        return [
            'fight',
        ]

    def sd_combat_seconds(self) -> float:
        return self.get_player().get_weapon().sd_attack_time()

    def gdo_create_form(self, form: GDT_Form) -> None:
        from gdo.shadowdogs.GDT_TargetArg import GDT_TargetArg
        form.add_field(
            GDT_TargetArg('target').foes(GDT_TargetArg.FOES_RANDOM).not_null().player(self.get_player()),
        )
        super().gdo_create_form(form)

    def get_target(self) -> 'SD_Player':
        return self.param_value('target')

    async def sd_execute(self):
        player = self.get_player()
        target = self.get_target()
        player.combat_stack().last_target = target
        await player.get_weapon().player(player).attack(target)
        return self.empty()
