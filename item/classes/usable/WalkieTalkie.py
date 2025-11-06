from gdo.message.GDT_HTML import GDT_HTML
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.city.y2064.Peine.locations.police.quest.JackPott import JackPott
from gdo.shadowdogs.item.classes.Usable import Usable
from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class WalkieTalkie(Usable):

    async def on_use(self, target: 'SD_Player|Obstacle|None'):
        q = JackPott.instance()
        if q.is_in_quest(self.get_owner()) or q.is_:
            await self.send_to_player(self.get_owner(), 'sdqs_police_nothing_new')
        else:
            await self.send_to_player(self.get_owner(), 'sdqs_police_surveilance_1')
            await self.send_to_player(self.get_owner(), 'sdqs_police_surveilance_2')
            await self.send_to_player(self.get_owner(), 'sdqs_police_surveilance_3')
            await q.accept()
        return GDT_HTML()
