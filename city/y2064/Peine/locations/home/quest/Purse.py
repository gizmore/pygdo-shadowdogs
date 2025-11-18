from gdo.shadowdogs.SD_Quest import SD_Quest


class Purse(SD_Quest):

    def reward(self) -> str|None:
        return 'Hash'

    def reward_source(self) -> str:
        from gdo.shadowdogs.city.y2064.Peine.locations.home.npc.Theodor import Theodor
        return Theodor.instance().render_name()
