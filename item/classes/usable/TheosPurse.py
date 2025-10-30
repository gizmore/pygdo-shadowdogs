from gdo.shadowdogs.city.y2064.Peine.locations.home.quest.Purse import Purse
from gdo.shadowdogs.item.classes.Usable import Usable

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.obstacle.Obstacle import Obstacle

class TheosPurse(Usable):

    async def on_use(self, target: 'SD_Player|Obstacle'):
        q = Purse.instance()
        c = int(q.qv_get('searched', '0')) + 1
        q.qv_set('searched', str(c))
        if c != 3:
            await self.send_to_player(self.get_player(), 'sdqa_purse_search')
        else:
            await self.send_to_player(self.get_player(), 'sdqa_purse_search_success')
            await self.give_new_items(self.get_player(), 'Hash', 'search', self.render_name())
            await q.accomplished()
