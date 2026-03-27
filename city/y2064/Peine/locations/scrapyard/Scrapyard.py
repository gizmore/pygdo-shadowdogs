from gdo.shadowdogs.locations.Location import Location


class Scrapyard(Location):

    async def on_search(self, player: 'SD_Player'):
        searched = int(self.lv_get('nt')) + 1
        if searched <= 8:
            await self.give_new_items(player, 'Wheel', 'search', self.render_name())
        else:
            await self.send_to_player(player, 'found_nothing')
        self.lv_set('nt', str(searched))
