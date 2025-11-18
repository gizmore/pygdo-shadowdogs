from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class status(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdstatus'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sds'


    def form_submitted(self):
        p = self.get_player()
        return self.reply('msg_sd_status', (
            p.render_gender(), p.render_race(),
            p.gb('p_level'), p.g('p_level'),
            p.gb('p_hp'), p.g('p_max_hp'),
            p.gb('p_mp'), p.g('p_max_mp'),
            p.g('p_attack'), p.g('p_defense'),
            p.g('p_marm'), p.g('p_farm'),
            p.g('p_min_dmg'), p.g('p_max_dmg'),
            p.gb('p_karma'), p.gb('p_xp'),
            p.g('p_weight') / 1000, p.weight.max_weight(p) / 1000,
            Shadowdogs.display_nuyen(p.get_nuyen()), Shadowdogs.display_nuyen(p.get_bank_nuyen()),
            p.gb('p_hunger')//10, p.gb('p_thirst')//10,
        ))
