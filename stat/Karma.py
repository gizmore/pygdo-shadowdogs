from gdo.shadowdogs.engine.Modifier import Modifier


class Karma(Modifier):

    def __init__(self, name: str):
        super().__init__(name)
        self.signed(False)
