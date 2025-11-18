from gdo.base.Trans import t
from gdo.base.Util import Arrays
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_Recipe import GDT_Recipe
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.item.data.recipe import recipe


class craft(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdcraft'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdcr'

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_Recipe('what').positional(),
        )
        super().gdo_create_form(form)

    def get_recipe(self) -> tuple[int, str]:
        return recipe.RECIPES.get(self.param_val('what'), None)

    async def sd_execute(self):
        player = self.get_player()
        if recipe_ := self.get_recipe():
            level, ingredients = recipe_
            item_names = ingredients.split(Shadowdogs.ITEM_SEPERATOR)
            if player.g('p_cra') < level:
                return self.err('err_sd_craft_level', (level, self.param_value('what')))
            if not self.has_ingredients(player, ingredients):
                return self.err('err_sd_craft_ingredients', (Arrays.human_join(item_names), self.param_value('what')))
            for item_name in item_names:
                player.inventory.remove_item(item_name).delete()
            await player.give_new_items(player, self.param_val('what'))
            return self.msg('msg_sd_crafted', (Arrays.human_join(item_names), t(self.param_value('what'))))
        else:
            out = []
            for what, recipe_ in recipe.RECIPES.items():
                level, ingredients = recipe_
                if player.g('p_cra') >= level and self.has_ingredients(player, ingredients):
                    out.append(t(what))
            if not out:
                return self.msg('msg_sd_craft_no_idea')
            return self.msg('msg_sd_craft_list', (len(out), Arrays.human_join(out)))

    def has_ingredients(self, player, ingredients):
        item_names = ingredients.split(Shadowdogs.ITEM_SEPERATOR)
        for item_name in item_names:
            if not player.inventory.has_item(item_name):
                return False
        return True

