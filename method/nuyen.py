from gdo.base.GDT import GDT
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.engine.MethodSD import MethodSD


class nuyen(MethodSD):

    def gdo_trigger(self) -> str:
        return "sdnuyen"

    def gdo_create_form(self, form: GDT_Form) -> None:
        super().gdo_create_form(form)

    def gdo_execute(self) -> GDT:
        per_player = []
        for player in self.get_party().members:
            per_player.append(f"{player.party_pos}-{player.render_name()}({player.render_ny()})")
        return self.msg('msg_sd_nuyen', (sum, ", ".join(per_player)))