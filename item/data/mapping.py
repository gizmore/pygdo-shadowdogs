import functools
from typing import Iterator, Tuple

from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs as Sd

class mapping:
    """
    field: (name, level, value, chance)
    """

    MATRIX = {
        "bod": (('rhino', 8, 1, Sd.RARE_LOW), ('anubis', 16, 2, Sd.RARE_MEDIUM), ('adonis', 24, 3, Sd.RARE_HIGH)),
        "mag": (('unicorn', 8, 1, Sd.RARE_LOW), ('isis', 16, 2, Sd.RARE_MEDIUM), ('medusa', 24, 3, Sd.RARE_HIGH)),
        "str": (('bear', 7, 1, Sd.RARE_LOW), ('horus', 16, 2, Sd.RARE_MEDIUM), ('goliath', 24, 3, Sd.RARE_HIGH)),
        "qui": (('gepard', 7, 1, Sd.RARE_LOW), ('shu', 16, 2, Sd.RARE_MEDIUM), ('chronos', 24, 3, Sd.RARE_HIGH)),
        "dex": (('monkey', 7, 1, Sd.RARE_LOW), ('nephthys', 16, 2, Sd.RARE_MEDIUM), ('odysseus', 24, 3, Sd.RARE_HIGH)),
        "int": (('raven', 7, 1, Sd.RARE_LOW), ('osiris', 16, 2, Sd.RARE_MEDIUM), ('prometheus', 24, 3, Sd.RARE_HIGH)),
        "wis": (('owl', 7, 1, Sd.RARE_LOW), ('thoth', 16, 2, Sd.RARE_MEDIUM), ('athena', 24, 3, Sd.RARE_HIGH)),
        "cha": (('peafowl', 7, 1, Sd.RARE_LOW), ('hathor', 16, 2, Sd.RARE_MEDIUM), ('aphrodite', 24, 3, Sd.RARE_HIGH)),
        "tra": (('bacchus', 7, 1, Sd.RARE_LOW), ('ptah', 16, 2, Sd.RARE_MEDIUM), ('mercury', 24, 3, Sd.RARE_HIGH)),
        "fig": (('lion', 7, 1, Sd.RARE_LOW), ('sekhmet', 16, 2, Sd.RARE_MEDIUM), ('ares', 24, 3, Sd.RARE_HIGH)),

        'max_weight': (('ant', 5, 1000, Sd.RARE_LOW),)
    }

    @classmethod
    def iter_entries(cls) -> Iterator[Tuple[str, str, int, int, int]]:
        """
        Yield (field, name, level, bonus, chance) for all entries.
        """
        for field, entries in cls.MATRIX.items():
            for name, level, bonus, chance in entries:
                yield (field, name, level, bonus, chance)

    @classmethod
    @functools.cache
    def get_fancy_word(cls, field: str, bonus: int) -> str:
        for f, name, level, b, chance in cls.iter_entries():
            if f == field and b == bonus:
                return name
        return None

    @classmethod
    @functools.cache
    def get_bonus(cls, name: str) -> int:
        for f, n, level, bonus, chance in cls.iter_entries():
            if n == name:
                return bonus
        return None

    @classmethod
    @functools.cache
    def get_field_name(cls, name: str) -> str:
        for f, n, level, bonus, chance in cls.iter_entries():
            if n == name:
                return f
        return None
