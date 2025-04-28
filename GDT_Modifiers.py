from gdo.base.Util import Strings
from gdo.core.GDT_String import GDT_String

from gdo.shadowdogs.attr.Attribute import Attribute
from gdo.shadowdogs.item.data.mapping import mapping
from gdo.shadowdogs.skill.Skill import Skill


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

    def validate(self, val: str|None) -> bool:
        if val:
            value = self.get_value()
            for word in value.keys():
                word = Strings.substr_to(word, ':', word)
                if not mapping.get_field_name(word) and f"p_{word}" not in Attribute.ATTRIBUTES and f"p_{word}" not in Skill.SKILLS:
                    self.error('err_sd_unknown_mods_mapping', (word,))
                    return False
        return super().validate(val)
