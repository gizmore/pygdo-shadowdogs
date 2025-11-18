from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_Course import GDT_Course
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.skill.Skill import Skill


class learn(MethodSD):

    def sd_is_location_specific(self) -> bool:
        return True

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_Course('course').not_null(),
        )
        super().gdo_create_form(form)

    def get_course(self) -> str:
        return self.param_value('course')

    async def sd_execute(self):
        return self.get_location().on_learn(self.get_player(), self.get_course())

