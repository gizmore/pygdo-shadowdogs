from gdo.base.Trans import Trans
from gdo.shadowdogs.engine.Factory import Factory
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.item.data.items import items
from gdo.shadowdogs.item.data.recipe import recipe
from gdo.shadowdogs.npcs.npcs import npcs
from gdo.shadowdogs.test.ShadowdogsTestCase import ShadowdogsTestCase
from gdotest.TestUtil import cli_plug


class ShadowdogsTest(ShadowdogsTestCase):

    async def test_00_creation(self):
        failure = True
        for item_name in items.ITEMS.keys():
            Factory.get_item(item_name)
            failure = False
        self.assertFalse(failure, 'Ooops')

    async def test_10_item_trans(self):
        for klass in items.ITEMS.keys():
            self.assertTrue(Trans.has(klass), f"Item {klass} has no trans #1")
            # self.assertTrue(Trans.has(klass+'_descr'), f"Item {klass} has no trans #2")

    async def test_20_recipe_items(self):
        for outcome, recipe_ in recipe.RECIPES.items():
            level, ingredients = recipe_
            item_names = ingredients.split(Shadowdogs.ITEM_SEPERATOR)
            self.assertTrue(Factory.get_item_by_arg(outcome), f"{outcome} is an unknown item!")
            for item_name in item_names:
                self.assertTrue(Factory.get_item_by_arg(item_name), f"{item_name} is unknown.")

    async def test_30_crafting(self):
        gizmore = await self.fresh_gizmore()
        out = cli_plug(gizmore, '$sdgmi giz 12xTwig')
        out = cli_plug(gizmore, '$sdcr')
        self.assertIn('no idea', out, 'craft no work #1.')
        self.sd_gizmore().increment('p_cra', 1).modify_all()
        out = cli_plug(gizmore, '$sdcr')
        self.assertIn('idea(s)', out, 'craft no work #2.')
        out = cli_plug(gizmore, '$sdcr fire')
        self.assertIn('crafted', out, 'craft no work #3.')
        out = cli_plug(gizmore, '$sdcr fire')
        self.assertIn('need 12xTwig', out, 'craft no work #4.')

    async def test_40_npc_items(self):
        failure = True
        for npc, data in npcs.NPCS.items():
            failure = False
            for item_name in data.get('eq', []):
                Factory.get_item_by_arg(item_name)
            for item_name in data.get('i', []):
                Factory.get_item_by_arg(item_name)
        self.assertFalse(failure, 'Ooops')

    async def test_50_location_search_items(self):
        failure = True
        for location in self.all_locations():
            if giving := location.GIVING:
                item_names = giving.split(Shadowdogs.ITEM_SEPERATOR)
                for item_name in item_names:
                    self.assertTrue(Factory.get_item_by_arg(item_name), f"{item_name} is unknown.")
                    failure = False
        self.assertFalse(failure, 'Ooops')






