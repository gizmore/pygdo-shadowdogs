from gdo.shadowdogs.locations.School import School
from gdo.shadowdogs.skill.Math import Math
from gdo.shadowdogs.skill.Skill import Skill


class GunzelinSchool(School):

    LESSONS: list[Skill] = [
        Math,
    ]

