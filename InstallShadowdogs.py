

class InstallShadowdogs:

    @classmethod
    def install(cls):
        from gdo.shadowdogs.SD_Player import SD_Player
        if not SD_Player.table().get_by_aid('1'):
            SD_Player.blank({
                'p_npc_klass': 'reaper',
                'p_race': 'dragon',
                'p_gender': 'male',
            }).insert()
