from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.item.classes.Usable import Usable
from typing import TYPE_CHECKING
from gdo.shadowdogs.item.data.recipe import recipe

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player
    from gdo.shadowdogs.obstacle.Obstacle import Obstacle


class Recipe(Usable):

    async def on_use(self, target: 'SD_Player|Obstacle|None'):
        if not isinstance(target, Item):
            return self.send_to_player(self.get_owner(), 'err_sd_craft_needs_item')
        for outcome, ingredients in recipe.RECIPES.values():
            a, b = ingredients
            if (self.get_name() == a and target.get_name() == b) or (self.get_name() == b and target.get_name() == a):
                return self.crafting(outcome, a, b)
        return self.send_to_player(self.get_owner(), 'err_sd_craft_no_work')
