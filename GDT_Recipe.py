from gdo.base.Trans import t
from gdo.core.GDT_Enum import GDT_Enum
from gdo.shadowdogs.item.data.recipe import recipe


class GDT_Recipe(GDT_Enum):

    def gdo_choices(self) -> dict:
        back = {}
        for outcome in recipe.RECIPES.keys():
            back[outcome] = t(outcome)
        return back
