from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodSD import MethodSD


class flee(MethodSD):

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdf'

    def sd_requires_action(self) -> list[str] | None:
        return [
            Action.FIGHT,
        ]

    def gdo_create_form(self, form: GDT_Form) -> None:
        super().gdo_create_form(form)

    def form_submitted(self):
        pass
