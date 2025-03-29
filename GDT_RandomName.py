from gdo.base.Util import Random
from gdo.core.GDT_String import GDT_String


class GDT_RandomName(GDT_String):

    SYLLABLES: list[str] = [
        'aar',
        'pet',
        'son'
    ]

    def get_val(self):
        name = ''
        n = Random.mrand(2, 4)
        for i in range(0, n):
            name += Random.list_item(self.SYLLABLES)
        return name
