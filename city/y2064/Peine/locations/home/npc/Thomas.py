from gdo.shadowdogs.npcs.TalkingMob import TalkingMob


class Thomas(TalkingMob):

    @classmethod
    def sd_npc_default_values(cls) -> dict[str, int]:
        return {
            'p_str': 2,
        }

    @classmethod
    def sd_npc_default_equipment(cls) -> list[str]:
        return [
            'Jeans',
            'Pullover',
            'Shoes',
        ]
