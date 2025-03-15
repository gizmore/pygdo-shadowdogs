from gdo.core.GDT_String import GDT_String

from typing import TYPE_CHECKING

class GDT_Modifiers(GDT_String):

    def __init__(self, name: str):
        super().__init__(name)
        self.ascii()
        self.case_s()

    def to_value(self, val: str):
        if not val:
            return None
        mods = {}
        for pair in val.split(','):
            data = pair.split(':')
            mods[data[0]] = data[1]
        return mods
