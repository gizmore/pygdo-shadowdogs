from gdo.shadowdogs.engine.Modifier import Modifier

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class Thirst(Modifier):

    def __init__(self, name: str):
        super().__init__(name)
        self.min(0)
        self.max(2000)
        self.bytes(2)
        self.initial('1000')

    def apply(self, target: 'SD_Player'):
        sat = self.get_value()
        malus = 0
        if sat > 1600:
            malus = -1
        if sat > 1800:
            malus = -3
        if malus:
            target.apply('p_qui', -malus)
            target.apply('p_dex', -malus)
