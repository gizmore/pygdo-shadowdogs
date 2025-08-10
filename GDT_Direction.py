from gdo.core.GDT_Enum import GDT_Enum


class GDT_Direction(GDT_Enum):

    _diagonal: bool

    def __init__(self, name: str):
        super().__init__(name)

    def diagonal(self, diagonal: bool=True):
        self._diagonal = diagonal
        return self

    def gdo_choices(self) -> dict:
        if self._diagonal:
            return {
                'r': 'Right',
                'dr': 'Down Right',
                'd': 'Down',
                'dl': 'Down Left',
                'l': 'Left',
                'ul': 'Up Left',
                'u': 'Up',
                'ur': 'Up Right',
            }
        else:
            return {
                'r': 'Right',
                'd': 'Down',
                'l': 'Left',
                'u': 'Up',
            }
