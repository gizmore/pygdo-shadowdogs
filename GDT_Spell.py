from psutil import STATUS_DISK_SLEEP

from gdo.core.GDT_Enum import GDT_Enum
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.spells.Spell import Spell
from gdo.shadowdogs.spells.calm import calm
from gdo.shadowdogs.spells.dart import dart


class GDT_Spell(WithShadowFunc, GDT_Enum):

    SPELLS: dict[str,Spell] = {
        'calm': calm(),
        'dart': dart(),
    }

    _known: bool

    def __init__(self, name: str):
        super().__init__(name)
        self.icon('magic')
        self.not_null()
        self._known = False

    def known(self, known: bool = True):
        self._known = known
        return self

    def gdo_choices(self) -> dict:
        if not self._known: return self.SPELLS
        from gdo.shadowdogs.SD_Spell import SD_Spell
        back = {}
        for name, spell in self.SPELLS.items():
            if SD_Spell.get_for_player(self.get_player(), name):
                back[name] = spell
        return back

    def to_value(self, val: str):
        from gdo.shadowdogs.SD_Spell import SD_Spell
        if value := super().to_value(val):
            if self._known:
                value.level(SD_Spell.get_for_player(self.get_player(), value.get_name()).get_level())
        return value
