from gdo.shadowdogs.engine.MethodSD import MethodSD


class status(MethodSD):

    def form_submitted(self):
        p = self.get_player()
        # You are a %male %elve level %d(%d). Atk: %d, Def: %d, Marm: %d, Farm: %d, MinDmg: %d, MaxDmg: %d. You have %d XP, %d Karma and carry %.01f from %.01f kg.
        return self.msg('msg_sd_status', (p.gdo_val('p_gender'), p.gdo_val('p_race'), p.gb('p_level'), p.g('p_level')))
