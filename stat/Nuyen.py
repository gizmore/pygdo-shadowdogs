from gdo.shadowdogs.engine.Modifier import Modifier
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class Nuyen(Modifier):

    def __init__(self, name: str):
        super().__init__(name)
        self.bytes(8)
        self.initial('0')
        self.not_null()

    def render(self):
        return self.get_value() + Shadowdogs.NUYEN
