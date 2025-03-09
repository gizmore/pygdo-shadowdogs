from gdo.core.GDT_String import GDT_String

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Player import GDO_Player

class GDT_Modifiers(GDT_String):

    def __init__(self, name: str):
        super().__init__(name)
        self.ascii()
        self.case_s()

    def apply(self, player: 'GDO_Player'):
        pass
