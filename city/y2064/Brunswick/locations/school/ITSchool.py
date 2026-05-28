from gdo.base.GDT import GDT
from gdo.shadowdogs.locations.School import School


class ITSchool(School):

    def sd_methods(self) -> list[str]:
        return [
            'sdcourses',
            'sdlearn',
            'sdwork',
        ]

    LESSONS: list[tuple[str, int]] = [
        ('Crypto', 3000),
        ('Hacking', 2000),
        ('Math', 1000),
    ]

    async def on_work(self) -> None:
        pass
