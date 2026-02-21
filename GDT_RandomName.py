from gdo.base.GDO import GDO
from gdo.base.Util import Random
from gdo.core.GDT_String import GDT_String

class GDT_RandomName(GDT_String):
    """
    A string field that generates a cool random name if no value is given.
    """

    PREFIXES = [
        'ar', 'bel', 'cor', 'dar', 'el', 'fal', 'gar', 'hal', 'han',
        'in', 'jor', 'kar', 'lor', 'mor', 'nel', 'or', 'pel',
        'quil', 'ras', 'sel', 'tor', 'ul', 'vor', 'wel', 'xer', 'yor', 'zer', 'zor',
    ]

    MIDDLES = [
        'dra', 'gra', 'kra', 'tra', 'sha', 'tha', 'pha', 'zha',
        'ael', 'iel', 'uel', 'oel', 'yel',
        'and', 'end', 'ond', 'und', 'ynd',
        'eth', 'ith', 'oth', 'uth', 'yth',
        'is', 'as', 'es', 'os', 'us',
    ]

    SUFFIXES = [
        'dor', 'mir', 'ran', 'thas', 'vyr', 'zor', 'dus', 'lak', 'nir', 'thul', 'rax', 'zoth', 'vash', 'mon',
    ]

    def gdo_before_create(self, gdo):
        if self.get_val() is None:
            self.generate_random_name(gdo)

    def generate_random_name(self, gdo: GDO):
        parts = []
        parts.append(Random.list_item(self.PREFIXES))
        middle_count = Random.mrand(0, 2)  # 0-2 middle parts
        for _ in range(middle_count):
            parts.append(Random.list_item(self.MIDDLES))
        parts.append(Random.list_item(self.SUFFIXES))
        name = ''.join(parts).capitalize()
        gdo.set_val(self._name, name)
