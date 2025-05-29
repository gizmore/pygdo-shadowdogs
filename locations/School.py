from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.skill.Skill import Skill


class School(Location):

    lessons: list[Skill] = []

    def sd_methods(self) -> list[str]:
        return [
            'sdcourses',
            'sdlearn',
        ]
    