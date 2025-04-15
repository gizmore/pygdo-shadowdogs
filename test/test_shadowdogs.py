import os
import unittest

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdo.shadowdogs.module_shadowdogs import module_shadowdogs
from gdotest.TestUtil import reinstall_module, WebPlug, GDOTestCase, cli_plug, cli_gizmore


class ShadowdogsTest(GDOTestCase):

    async def ticker(self, ticks: int=1):
        for i in range(1, ticks):
            await module_shadowdogs.instance().shadow_timer()
            await module_shadowdogs.instance().shadow_hp_timer()

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
        self.assertIn('You created your character', out, 'sdstart throws no error.')
        out = cli_plug(gizmore, '$sdgdt gizmore{1} lamer,lamer')
        self.assertIn('encounter', out, 'gdt does not work.')
        await self.ticker(10)
        self.assertIn('hit', out, 'attack no work')
        


if __name__ == '__main__':
    unittest.main()
