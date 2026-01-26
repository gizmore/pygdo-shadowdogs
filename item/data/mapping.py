import functools
from typing import Iterator, Tuple

from gdo.base.Util import Strings
from gdo.shadowdogs.attr.Attribute import Attribute
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs as Sd
from gdo.shadowdogs.skill.Skill import Skill


class mapping:
    """
    field: (name, level, value, chance)
    """

    MATRIX = { # TODO greek in the middle, egypt best
        "p_bod": (('rhino',   8, 1, Sd.RARE_LOW), ('anubis',   16, 2, Sd.RARE_MEDIUM), ('adonis',     24, 3, Sd.RARE_HIGH)),
        "p_mag": (('unicorn', 8, 1, Sd.RARE_LOW), ('isis',     16, 2, Sd.RARE_MEDIUM), ('medusa',     24, 3, Sd.RARE_HIGH)),
        "p_str": (('bear',    7, 1, Sd.RARE_LOW), ('horus',    16, 2, Sd.RARE_MEDIUM), ('goliath',    24, 3, Sd.RARE_HIGH)),
        "p_qui": (('gepard',  7, 1, Sd.RARE_LOW), ('shu',      16, 2, Sd.RARE_MEDIUM), ('chronos',    24, 3, Sd.RARE_HIGH)),
        "p_dex": (('monkey',  7, 1, Sd.RARE_LOW), ('nephthys', 16, 2, Sd.RARE_MEDIUM), ('odysseus',   24, 3, Sd.RARE_HIGH)),
        "p_int": (('raven',   6, 1, Sd.RARE_LOW), ('osiris',   16, 2, Sd.RARE_MEDIUM), ('prometheus', 24, 3, Sd.RARE_HIGH)),
        "p_wis": (('owl',     6, 1, Sd.RARE_LOW), ('thoth',    16, 2, Sd.RARE_MEDIUM), ('athena',     24, 3, Sd.RARE_HIGH)),
        "p_cha": (('peafowl', 6, 1, Sd.RARE_LOW), ('hathor',   16, 2, Sd.RARE_MEDIUM), ('aphrodite',  24, 3, Sd.RARE_HIGH)),
        "p_tra": (('bacchus', 6, 1, Sd.RARE_LOW), ('ptah',     16, 2, Sd.RARE_MEDIUM), ('mercury',    24, 3, Sd.RARE_HIGH)),
        "p_fig": (('lion',    6, 1, Sd.RARE_LOW), ('sekhmet',  16, 2, Sd.RARE_MEDIUM), ('ares',       24, 3, Sd.RARE_HIGH)),

        "p_attack":  (('tiger', 10, 1, Sd.RARE_MEDIUM),  ('papyrus', 20, 3, Sd.RARE_HIGH), ('troy',    30, 6, Sd.RARE_ULTRA)),
        "p_defense": (('turtle', 13, 1, Sd.RARE_MEDIUM), ('mirror',  26, 2, Sd.RARE_HIGH), ('phalanx', 38, 4, Sd.RARE_ULTRA)),

        "p_marm": (('turtle', 11, 1, Sd.RARE_MEDIUM), ('tomb', 20, 2, Sd.RARE_HIGH), ('wall', 30, 3, Sd.RARE_ULTRA),),
        "p_farm": (('squid',  12, 1, Sd.RARE_MEDIUM), ('reed', 24, 2, Sd.RARE_HIGH), ('oil', 36, 3, Sd.RARE_ULTRA),),

        'p_max_weight': (('ant', 5, 2000, Sd.RARE_NO), ('scarab', 13, 4000, Sd.RARE_MEDIUM)),
    }

    @classmethod
    def iter_entries(cls) -> Iterator[Tuple[str, str, int, int, int]]:
        """
        Yield (field, name, level, bonus, chance) for all entries.
        """
        for field in cls.MATRIX.keys():
            yield from cls.iter_entries_for_field(field)

    @classmethod
    def iter_entries_for_field(cls, field: str) -> Iterator[Tuple[str, str, int, int, int]]:
        """
        Yield (field, name, level, bonus, chance) for all entries.
        """
        for name, level, bonus, chance in cls.MATRIX.get(field):
            yield field, name, level, bonus, chance

    @classmethod
    @functools.cache
    def get_fancy_word(cls, field: str, bonus: int) -> str:
        for f, name, level, b, chance in cls.iter_entries():
            if f == field and b == bonus:
                return name
        return None

    @classmethod
    @functools.cache
    def get_all_bonus(cls, name: str) -> dict[str, int]:
        return {field: bonus for field, name, level, bonus, chance in cls.iter_entries()}

    @classmethod
    @functools.cache
    def get_bonus(cls, name: str) -> int:
        for f, n, level, bonus, chance in cls.iter_entries():
            if n == name:
                return bonus
        return 0

    @classmethod
    @functools.cache
    def get_field_name(cls, name: str) -> str:
        for f, n, level, bonus, chance in cls.iter_entries():
            if n == name:
                return f
        return f"p_{name}"

    @classmethod
    def is_valid(cls, mods: str) -> bool:
        if mods:
            for mod in mods.split(','):
                mod = Strings.substr_to(mod, ':', mod).lower()
                if not cls.get_field_name(mod) and not mod in Attribute.ATTRIBUTES and not mod in Skill.SKILLS:
                    return False
        return True
