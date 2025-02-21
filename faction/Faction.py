from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Creator import GDT_Creator
from gdo.core.GDT_Name import GDT_Name
from gdo.date.GDT_Created import GDT_Created


class Faction(GDO):
    BONUS = {
        'freeborn': {'bod': 10, 'mag': 10, 'str': 4, 'int': 5, 'dex': 5, 'qui': 5, 'cha': 5, 'tra': 5, 'hac': 8, 'cry': 9, 'mat': 9, 'fig': 0},
        'consort': {'bod': 10, 'mag': 10, 'str': 4, 'int': 5, 'dex': 5, 'qui': 5, 'cha': 5, 'tra': 5, 'hac': 6, 'cry': 7, 'mat': 7, 'fig': 0},
        'seeker': {'bod': 10, 'mag': 10, 'str': 4, 'int': 6, 'dex': 5, 'qui': 5, 'cha': 6, 'tra': 5, 'hac': 7, 'cry': 8, 'mat': 8, 'fig': 7},
        'aegis': {'bod': 10, 'mag': 10, 'str': 6, 'int': 5, 'dex': 5, 'qui': 5, 'cha': 4, 'tra': 5, 'hac': 5, 'cry': 6, 'mat': 6, 'fig': 10},
    }

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('faction_id'),
            GDT_Name('faction_name'),
            GDT_Creator('faction_creator'),
            GDT_Created('faction_created'),
        ]
