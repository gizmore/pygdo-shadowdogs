from gdo.base.GDT import GDT
from gdo.base.Trans import t
from gdo.message.GDT_HTML import GDT_HTML
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.locations.Location import Location


class School(Location):

    LESSONS: list[tuple[str, int]] = GDT.EMPTY_LIST

    def sd_methods(self) -> list[str]:
        return [
            'sdcourses',
            'sdlearn',
        ]

    def sd_courses(self, player: 'SD_Player') -> list[tuple[str, int]] :
        return self.LESSONS

    async def on_courses(self, player: 'SD_Player') -> GDT:
        courses = []
        for course, price in self.sd_courses(player):
            courses.append(f"{self.t(course)}({Shadowdogs.display_nuyen(price)})")
        if courses:
            await self.send_to_player(player, 'msg_sd_courses', (", ".join(courses),))
        else:
            await self.send_to_player(player, 'msg_sd_no_courses')
        return GDT_HTML()

    async def on_learn(self, player: 'SD_Player', course: str) -> GDT:
        for c, price in self.sd_courses(player):
            if course == t(c):
                if player.gb(c) < -1:
                    await self.send_to_player(player, 'err_sd_learn_impossible', (self.t(course),))
                elif not player.has_nuyen(price):
                    await self.send_to_player(player, 'err_sd_learn_money', (Shadowdogs.display_nuyen(price), self.t(course), Shadowdogs.display_nuyen(player.get_nuyen())))
                else:
                    player.give_nuyen(-price)
                    player.incb(c, 1).save()
                    await self.send_to_player(player, 'msg_sd_learned', (Shadowdogs.display_nuyen(price), course, player.gb(c), Shadowdogs.display_nuyen(player.get_nuyen())))
            return GDT_HTML()
        return GDT_HTML()
