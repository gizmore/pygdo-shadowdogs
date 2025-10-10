from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_LocationTarget import GDT_LocationTarget
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.locations.Location import Location


class goto(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdgoto'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdg'

    def sd_is_leader_command(self) -> bool:
        return True

    def sd_requires_action(self) -> list[str] | None:
        return [
            Action.INSIDE,
            Action.OUTSIDE,
            Action.GOTO,
            Action.EXPLORE,
        ]

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_LocationTarget('to').known().same_city().not_null(),
        )
        super().gdo_create_form(form)

    def get_target(self) -> Location:
        return self.param_value('to')

    async def sd_execute(self):
        t = self.get_target()
        p = self.get_party()
        await p.do(Action.GOTO, t.get_location_key(), p.calc_goto_eta_s(t))
        return self.empty()
