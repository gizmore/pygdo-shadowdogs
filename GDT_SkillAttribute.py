from gdo.base.Trans import t
from gdo.core.GDT_Enum import GDT_Enum
from gdo.shadowdogs.attr.Attribute import Attribute
from gdo.shadowdogs.skill.Skill import Skill


class GDT_SkillAttribute(GDT_Enum):

    _skills: bool
    _attributes: bool

    def __init__(self, name: str):
        super().__init__(name)
        self._skills = False
        self._attributes = False

    def skills(self, skills=True):
        self._skills = skills
        return self

    def attributes(self, attributes=True):
        self._attributes = attributes
        return self

    def gdo_choices(self) -> dict:
        back = {}
        if self._skills:
            for skill in Skill.SKILLS:
                back[skill] = t(skill)
        if self._attributes:
            for attr in Attribute.ATTRIBUTES:
                back[attr] = t(attr)
        return back

    def is_attribute(self, attr: str) -> bool:
        return attr in Attribute.ATTRIBUTES

    def is_skill(self, skill: str) -> bool:
        return skill in Skill.SKILLS
