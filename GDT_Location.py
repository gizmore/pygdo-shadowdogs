from gdo.core.GDT_String import GDT_String


class GDT_Location(GDT_String):

    _known: bool

    def __init__(self, name: str):
        super().__init__(name)

    def known(self, known: bool=True):
        self._known = known
        return self



