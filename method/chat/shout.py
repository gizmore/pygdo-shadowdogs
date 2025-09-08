from gdo.core.GDT_RestOfText import GDT_RestOfText
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.engine.MethodSD import MethodSD


class shout(MethodSD):

    SHOUT_KEY = 'sd_shout'

    LAST_SHOUTS: dict[str,int] = {}

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdshout'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdsh'

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_RestOfText('message').not_null(),
        )

    def sd_execute(self):
        player = self.get_player()
        player.set_temp(self.get_time())
        self.send_to_all('msg_sd_shout', (player.render_name(), self.param_value('message')))
