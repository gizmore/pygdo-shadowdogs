from gdo.shadowdogs.engine.Modifier import Modifier
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs


class Nuyen(Modifier):

    def __init__(self, name: str):
        super().__init__(name)
        self.bytes(4)

    def render(self):
        return self.get_value() + Shadowdogs.NUYEN
