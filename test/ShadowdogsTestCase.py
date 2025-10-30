import os

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdo.core.method.clear_cache import clear_cache
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.table.module_table import module_table
from gdotest.TestUtil import GDOTestCase, reinstall_module, WebPlug, cli_gizmore, cli_plug


class ShadowdogsTestCase(GDOTestCase):

    def setUp(self):
        super().setUp()
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        loader = ModuleLoader.instance()
        loader.load_modules_db(True)
        reinstall_module('shadowdogs')
        clear_cache().gdo_execute()
        WebPlug.COOKIES = {}
        Application.init_cli()
        loader.init_modules(True, True)
        loader.init_cli()
        module_table.instance().save_config_val('table_ipp', '4')

    def sd_gizmore(self):
        gizmore = cli_gizmore()
        return Shadowdogs.USERMAP[gizmore.get_id()]

    async def fresh_gizmore(self, equip: bool = True):
        gizmore = cli_gizmore()
        out = cli_plug(gizmore, '$sdenable')
        self.assertIn('has been enabled', out, 'sdenable does not work.')
        out = cli_plug(gizmore, '$sdreset --confirm=1')
        self.assertIn('e', out, 'sdreset does not work.')
        out = cli_plug(gizmore, '$sdstart elf mail')
        self.assertIn('Suggestions', out, 'sdstart throws no error.')
        out = cli_plug(gizmore, '$sdstart male human')
        self.assertIn('You created your character', out, 'sdstart throws an error.')
        out = cli_plug(gizmore, '$sdsearch')
        self.assertIn('12', out, 'search does not work.')
        out = cli_plug(gizmore, '$sdgmi gizmore{1} club_of_adonis')
        self.assertIn('received Club_of_Adonis', out, 'gmi does not work.')
        if equip:
            out = cli_plug(gizmore, '$sdeq club')
            await self.ticker_for()
            out += cli_plug(gizmore, '$sdi')
            await self.ticker_for()
            out += cli_plug(gizmore, '$sdq')
            await self.ticker_for()
            self.assertIn('You use', out, 'eq does not work.')
            self.assertIn('Club_of', out, 'eq does not work.#2')
            out = cli_plug(gizmore, '$sdeq shoe')
            await self.ticker_for()
            out = cli_plug(gizmore, '$sdeq jean')
            await self.ticker_for()
        return gizmore
