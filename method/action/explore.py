from gdo.base.Application import Application
from gdo.base.Render import Mode
from gdo.base.Trans import t
from gdo.date.Time import Time
from gdo.form.GDT_Form import GDT_Form
from gdo.form.MethodForm import MethodForm
from gdo.shadowdogs.SD_Party import SD_Party
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.GDT_City import GDT_City
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodSD import MethodSD


class explore(MethodSD):

    def sd_is_leader_command(self) -> bool:
        return True

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdexplore'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdexp'

    # def gdo_create_form(self, form: GDT_Form) -> None:
    #     form.add_field(
    #         GDT_City('area').known().not_null(),
    #     )
    #     super().gdo_create_form(form)

    def form_submitted(self):
        pa = self.get_party()
        city = self.get_city()
        pa.do(Action.EXPLORE, city.get_name(), city.get_explore_eta(pa))
        return self.empty()
