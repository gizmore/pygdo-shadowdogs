from gdo.core.GDT_String import GDT_String

from typing import TYPE_CHECKING

from gdo.shadowdogs.item.data.mapping import mapping


class GDT_Modifiers(GDT_String):
    """
    A generic additional modifier field.
    value is a dict[str,int]
    val is a string modifer1,modifier2
    """

    def __init__(self, name: str):
        super().__init__(name)
        self.ascii()
        self.case_s()

    def to_val(self, value) -> str:
        join_me = []
        for key, val in value.items():
            if fancy := mapping.get_fancy_word(key, val):
                join_me.append(fancy)
            else:
                join_me.append(f"{key}:{val}")
        return ",".join(join_me)

    def to_value(self, val: str):
        if not val:
            return None
        mods = {}
        for pair in val.split(','):
            data = pair.split(':')
            mods[mapping.get_field_name(data[0])] = int(data[1]) if len(data) > 1 else mapping.get_bonus(data[0])
        return mods
