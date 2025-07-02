from gdo.core.GDT_Enum import GDT_Enum


class GDT_Direction(GDT_Enum):

    def __init__(self, name: str):
        super().__init__(name)
        self.choices({
            'r': 'Right',
            'u': 'Up',
            'd': 'Down',
            'l': 'Left',
        })
