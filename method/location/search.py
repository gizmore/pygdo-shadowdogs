from gdo.core.GDO_User import GDO_User
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_TargetArg import GDT_TargetArg
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class search(MethodSD):

    def sd_is_location_specific(self) -> bool:
        return True

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_TargetArg('target').gdo(self.get_player()).default_room().obstacles(),
        )
        super().gdo_create_form(form)

    def get_target(self) -> Obstacle|Location:
        return self.param_value('target')

    def form_submitted(self):
        what = self.get_target()
        what.on_search(self.get_player())
        return self.empty()
