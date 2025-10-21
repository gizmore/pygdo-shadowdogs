from gdo.core.GDT_Enum import GDT_Enum
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.locations.School import School


class GDT_Course(WithShadowFunc, GDT_Enum):

    def get_school(self) -> School:
        return self.get_location()

    def gdo_choices(self) -> dict:
        choices = {}
        for course, price in self.get_location().sd_courses(self.get_player()):
            choices[course] = self.t(course)
        return choices

