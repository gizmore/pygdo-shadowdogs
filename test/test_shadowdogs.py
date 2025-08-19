import asyncio
import os
import unittest

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdo.base.Util import Random
from gdo.core.GDO_User import GDO_User
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.module_shadowdogs import module_shadowdogs
from gdo.table.module_table import module_table
from gdotest.TestUtil import reinstall_module, WebPlug, GDOTestCase, cli_plug, cli_gizmore, all_private_messages


class ShadowdogsTest(GDOTestCase):

    TICKS: int = 0

    async def ticker_for(self, user: 'GDO_User'=None):
        user = user or cli_gizmore()
        await self.ticker(Shadowdogs.USERMAP[user.get_id()].get_busy_seconds()+2)

    async def ticker(self, ticks: int=1):
        print(f"{ticks} ticks pass buy.")
        for i in range(0, ticks-1):
            i = self.TICKS + i
            Application.TIME += 1
            await Application.EVENTS.update_timers(module_shadowdogs.instance().cfg_time())
        self.TICKS += ticks

    def setUp(self):
        super().setUp()
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        loader = ModuleLoader.instance()
        loader.load_modules_db(True)
        reinstall_module('shadowdogs')
        WebPlug.COOKIES = {}
        Application.init_cli()
        loader.init_modules(True, True)
        loader.init_cli()
        module_table.instance().save_config_val('table_ipp', '3')

    async def fresh_gizmore(self, equip: bool=True):
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
        if equip:
            out = cli_plug(gizmore, '$sdeq 1')
            await self.ticker_for()
            out += cli_plug(gizmore, '$sdi')
            await self.ticker_for()
            out += cli_plug(gizmore, '$sdeq 1')
            await self.ticker_for()
            out += cli_plug(gizmore, '$sdeq 1')
            await self.ticker_for()
            out += cli_plug(gizmore, '$sdeq 1')
            await self.ticker_for()
            out += cli_plug(gizmore, '$sdq')
            await self.ticker_for()
            self.assertIn('You use Jeans as your', out, 'gmq does not work.')
        return gizmore

    async def test_00_start(self):
        gizmore = await self.fresh_gizmore(False)
        out = cli_plug(gizmore, '$sdi')
        self.assertIn('page 1 of 2', out, '$sdi does not work.')
        out = cli_plug(gizmore, '$sdi 2')
        self.assertIn('page 2 of 2', out, '$sdi 2 does not work.')
        self.assertIn('Club_of_adonis', out, '$sdi 2 does not render.')
        out = cli_plug(gizmore, '$sdeq _of_ado')
        await self.ticker(121)
        out += all_private_messages()
        self.assertIn('Club_of_adonis as ', out, 'eq does not work.')
        out = cli_plug(gizmore, '$sdq')
        self.assertIn('Weapon: Club_of_adonis', out, '$sdq does not work.')
        Random.init(9)
        out = cli_plug(gizmore, '$sdgmt gizmore{1} lamer')
        self.assertIn('encounter', out, 'gmt does not work.')
        await self.ticker(160)
        out = all_private_messages()
        self.assertIn('kills', out, 'attack does not work.')

    async def test_01_hack(self):
        gizmore = await self.fresh_gizmore()
        out = cli_plug(gizmore, '$sdgmi gizmore{1} RhinoDeck')
        self.assertIn('received', out, 'gmi#1 does not work.')
        out = cli_plug(gizmore, '$sdgmi gizmore{1} Ping4.exe')
        self.assertIn('received', out, 'gmi#2 does not work.')
        out = cli_plug(gizmore, '$sdeq Rhino')
        self.assertIn('RhinoDeck', out, 'eq#1 does not work.')
        await self.ticker(60)
        out = all_private_messages()
        out += cli_plug(gizmore, '$sdlook')
        self.assertIn('PC', out, 'look does not work.')
        out = cli_plug(gizmore, '$sdhack')
        self.assertIn('PC', out, 'hack does not work.')
        out = cli_plug(gizmore, '$sdmov r')
        self.assertIn('free', out, 'movr#1 does not work.')
        out = cli_plug(gizmore, '$sdmov r')
        self.assertIn('vault', out, 'movr#2 does not work.')

    async def test_02_info(self):
        cli_plug(cli_gizmore(), '$sdenable')
        out = cli_plug(cli_gizmore(), '$sdi')
        self.assertIn('sdstart first', out, 'Player check not working')
        gizmore = await self.fresh_gizmore()
        out = cli_plug(cli_gizmore(), '$sdi')
        self.assertIn('nventory', out, '$sdi not working')


    async def test_03_eat(self):
        gizmore = await self.fresh_gizmore()
        out = cli_plug(gizmore, '$sdgmi giz Sandwich')
        self.assertIn('receive', out, 'gmi does not work.')
        out = cli_plug(gizmore, '$sds')
        self.assertIn('not hungry', out, 'not hungry?')
        out = cli_plug(gizmore, '$sduse Sandwich')
        self.assertIn('consumed', out, 'eat sandwich does not work.')
        out = cli_plug(gizmore, '$sds')
        self.assertIn('not hungry', out, 'hungry?')

    async def test_05_combat1(self):
        gizmore = await self.fresh_gizmore(True)
        out = cli_plug(gizmore, '$sdgmt noob')
        pass

    async def test_09_explore(self):
        gizmore = await self.fresh_gizmore()
        out = cli_plug(gizmore, '$sdeq Shir')
        await self.ticker_for()
        out = cli_plug(gizmore, '$sdeq Sand')
        await self.ticker(160)
        out = cli_plug(gizmore, '$sdeq Jean')
        await self.ticker(160)
        out = cli_plug(gizmore, '$sdeq _of_ado')
        await self.ticker(160)
        Random.init(1337)
        out = cli_plug(gizmore, '$sdexplore')
        self.assertIn('start to explore', out, 'explore does not work.')
        out = cli_plug(gizmore, '$sdp')
        self.assertIn('exploring Peine', out, 'party does not work.')
        await self.ticker(2400) # half an hour
        out = all_private_messages()
        self.assertIn('new place in Peine', out, 'explore find does not work.')
        out = cli_plug(gizmore, '$sdpl')
        self.assertIn('2 locations in Peine', out, 'kp does not work.')


if __name__ == '__main__':
    unittest.main()
