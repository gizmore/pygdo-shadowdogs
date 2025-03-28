from gdo.core.GDT_UInt import GDT_UInt


class Modifier(GDT_UInt):

    def __init__(self, name: str):
        super().__init__(name)
        self.bytes(2)
        self.not_null()
        self.initial('0')

    def apply(self, target: 'Player'):
        raise Exception(f"Modifier {self.__class__.__name__} has no apply.")
