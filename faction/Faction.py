from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Creator import GDT_Creator
from gdo.core.GDT_Name import GDT_Name
from gdo.date.GDT_Created import GDT_Created


class Faction(GDO):

    BONUS = {
        'freeborn':   {'st': 4, 'in': 5, 'dx': 5, 'qu': 5, 'ch': 5, 'bo': 10, 'ma': 10 },    # Freedom  |(magic + in)
        'concordium':   {'st': 4, 'in': 5, 'dx': 5, 'qu': 5, 'ch': 5, 'bo': 10, 'ma': 10 },  # Peace    |(trading + magic)
        'seekers':   {'st': 4, 'in': 5, 'dx': 5, 'qu': 5, 'ch': 5, 'bo': 10, 'ma': 10 },     # Truth    |(trading + influence)
        'iron':   {'st': 4, 'in': 5, 'dx': 5, 'qu': 5, 'ch': 5, 'bo': 10, 'ma': 10 },        # War      |(influence + st + dx)
    }

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('faction_id'),
            GDT_Name('faction_name'),
            GDT_Creator('faction_creator'),
            GDT_Created('faction_created'),
        ]
