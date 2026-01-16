from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.npcs.Hireling import Hireling


class Mike(Hireling):

    @classmethod
    def sd_hireling_base(cls) -> dict[str, int | str]:
        return {
            'p_level': '3',
            'p_race': 'human',
            'p_gender': 'male',
        }

    @classmethod
    def sd_hireling_items(cls) -> list[str]:
        return []

    @classmethod
    def sd_hireling_bonus(cls) -> dict[str, int | str]:
        return {
            'p_str': 3,
            'p_qui': 3,
        }

    async def on_say(self, player: SD_Player, text: str):
        pass
