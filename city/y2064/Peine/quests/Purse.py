from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class Purse(SD_Quest):

    def reward(self) -> str|None:
        return 'Dope'

    def reward_source(self) -> str:
        from gdo.shadowdogs.city.y2064.Peine.npcs.home.Theodor import Theodor
        return Shadowdogs.get_npc(Theodor).render_name()
