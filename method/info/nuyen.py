from gdo.base.GDT import GDT
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class nuyen(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return "sdnuyen"

    @classmethod
    def gdo_trig(cls) -> str:
        return "sdny"

    def gdo_create_form(self, form: GDT_Form) -> None:
        super().gdo_create_form(form)

    def gdo_execute(self) -> GDT:
        sum = 0
        per_player = []
        for player in self.get_party().members:
            per_player.append(f"{player.party_pos}-{player.render_name()}({Shadowdogs.display_nuyen(player.get_nuyen())})")
            sum += player.get_nuyen()
        return self.msg('msg_sd_nuyen', (sum, ", ".join(per_player)))
