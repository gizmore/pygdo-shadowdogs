import os
import unittest

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.module_shadowdogs import module_shadowdogs
from gdo.table.module_table import module_table
from gdotest.TestUtil import reinstall_module, WebPlug, GDOTestCase, cli_plug, cli_gizmore, all_private_messages


class ShadowdogsTest(GDOTestCase):

    TICKS: int = 0

    async def ticker(self, ticks: int=1):
        for i in range(0, ticks-1):
            i = self.TICKS + i
            if (i % Shadowdogs.SECONDS_PER_TICK) == 0:
                await module_shadowdogs.instance().shadow_timer()
            if (i % Shadowdogs.SECONDS_PER_HP_SLEEP) == 0:
                await module_shadowdogs.instance().shadow_hp_timer()
            if (i % Shadowdogs.SECONDS_PER_FOODING) == 0:
                await module_shadowdogs.instance().shadow_food_timer()
        self.TICKS += ticks

    def setUp(self):
        super().setUp()
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        reinstall_module('shadowdogs')
        loader = ModuleLoader.instance()
        loader.load_modules_db(True)
        loader.init_modules(True, True)
        WebPlug.COOKIES = {}
        Application.init_cli()
        loader.init_cli()
        module_table.instance().save_config_val('table_ipp', '3')

    async def test_00_start(self):
        gizmore = cli_gizmore()
        # channel = gizmore.get_server().get_or_create_channel('gizmore')
        out = cli_plug(gizmore, '$sdenable')
        self.assertIn('has been enabled', out, 'sdenable does not work.')
        out = cli_plug(gizmore, '$sdreset --confirm=1')
        self.assertIn('e', out, 'sdreset does not work.')
        out = cli_plug(gizmore, '$sdstart elf mail')
        self.assertIn('Suggestions', out, 'sdstart throws no error.')
        out = cli_plug(gizmore, '$sdstart male human')
        self.assertIn('You created your character', out, 'sdstart throws an error.')
        out = cli_plug(gizmore, '$sdgmi gizmore{1} club_of_adonis')
        self.assertIn('received Club_of_adonis', out, 'gmi does not work.')
        out = cli_plug(gizmore, '$sdi')
        self.assertIn('page 1 of 2', out, '$sdi does not work.')
        out = cli_plug(gizmore, '$sdi 2')
        self.assertIn('page 2 of 2', out, '$sdi 2 does not work.')
        self.assertIn('1m5', out, '$sdi 2 does not render.')
        out = cli_plug(gizmore, '$sdeq _of_ado')
        self.assertIn('Club_of_adonis as ', out, 'eq does not work.')
        out = cli_plug(gizmore, '$sdq')
        self.assertIn('Weapon: Club_of_adonis', out, '$sdq does not work.')
        out = cli_plug(gizmore, '$sdgmt gizmore{1} lamer,lamer')
        self.assertIn('encounter', out, 'gmt does not work.')
        await self.ticker(121)
        out = all_private_messages()
        self.assertIn('hit', out, 'attack does not work.')



if __name__ == '__main__':
    unittest.main()
