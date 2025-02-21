from gdo.core.GDT_UInt import GDT_UInt


class Modifier(GDT_UInt):

    def __init__(self, name: str):
        super().__init__(name)

    def apply(self, target: 'Player'):

        pass
