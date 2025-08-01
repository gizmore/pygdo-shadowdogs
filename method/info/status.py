from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class status(MethodSD):

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sds'

    def form_submitted(self):
        p = self.get_player()
        return self.reply('msg_sd_status', (
            p.render_gender(), p.render_race(),
            p.g('p_hp'), p.g('p_max_hp'),
            p.g('p_mp'), p.g('p_max_mp'),
            p.gb('p_level'), p.g('p_level'),
            p.g('p_attack'), p.g('p_defense'),
            p.g('p_marm'), p.g('p_farm'),
            p.g('p_min_dmg'), p.g('p_max_dmg'),
            p.gb('p_xp'), p.g('p_karma'),
            p.g('p_weight'), p.g('p_max_weight'),
            Shadowdogs.display_nuyen(p.g('p_nuyen')),
            Shadowdogs.display_nuyen(p.g('p_bank_nuyen')),
        ))
