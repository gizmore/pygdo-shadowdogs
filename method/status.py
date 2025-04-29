from gdo.shadowdogs.engine.MethodSD import MethodSD


class status(MethodSD):

    def form_submitted(self):
        p = self.get_player()
        return self.msg('msg_sd_status', (
            p.render_gender(), p.render_race(),
            p.gb('p_level'), p.g('p_level'),
            p.g('p_attack'), p.g('p_defense'),
            p.g('p_marm'), p.g('p_farm'),
            p.g('p_min_dmg'), p.g('p_max_dmg'),
            p.gb('p_xp'), p.g('p_karma'),
            p.g('p_weight'), p.g('p_max_weight'),
            p.g('p_nuyen'), p.g('p_bank_nuyen'),
        ))
