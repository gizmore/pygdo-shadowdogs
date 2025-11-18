from gdo.shadowdogs.city.y2064.Peine.locations.gunzelin.Miehe import Miehe
from gdo.shadowdogs.locations.School import School
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class GunzelinSchool(School):

    NPCS: 'list[type[TalkingNPC]]' = [
        Miehe,
    ]

    LESSONS: list[tuple[str, int]] = [
        ('p_mat', 350),
    ]
