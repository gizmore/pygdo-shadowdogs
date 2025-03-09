from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.base.Render import Mode
from gdo.form.GDT_Form import GDT_Form
from gdo.form.MethodForm import MethodForm
from gdo.shadowdogs.GDO_Player import GDO_Player
from gdo.shadowdogs.GDT_Race import GDT_Race
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.user.GDT_Gender import GDT_Gender


class start(WithShadowFunc, MethodForm):

    def gdo_trigger(self) -> str:
        return 'sdstart'

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_Race('race').not_null(),
            GDT_Gender('gender').simple().not_null(),
        )
        super().gdo_create_form(form)

    def form_submitted(self):
        if player := self.get_player():
            return self.err('err_sd_already_started')
        player = GDO_Player.blank({
            'p_race': self.param_val('race'),
            'p_gender': self.param_val('gender'),
        }).insert()
        return self.msg('msg_sd_started', (
            player.gdo_column('p_race').render(self._env_mode),
            player.gdo_column('p_gender').render(self._env_mode)))
