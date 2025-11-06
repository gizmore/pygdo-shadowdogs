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
            GDT_Recipe('what').not_null(),
        )
        super().gdo_create_form(form)

    def get_recipe(self) -> tuple[int, str]:
        return recipe.RECIPES[self.param_val('what')]

    def sd_execute(self):
        level, ingredients = self.get_recipe()
        player = self.get_player()
        if player.g('p_cra') < level:
            return self.err('err_sd_craft_level', (level, self.param_value('what')))
        item_names = ingredients.split(Shadowdogs.ITEM_SEPERATOR)
        for item_name in item_names:
            if not player.inventory.has_item(item_name):
                return self.err('err_sd_craft_ingredients', (Arrays.human_join(item_names), self.param_value('what')))
        for item_name in item_names:
            player.inventory.remove_item(item_name)
        return self.msg('msg_sd_crafted', (Arrays.human_join(item_names), self.param_value('what')))
