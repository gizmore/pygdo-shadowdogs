import os
import unittest

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdo.base.Util import Random
from gdo.core.method.clear_cache import clear_cache
from gdo.shadowdogs.engine.Factory import Factory
from gdo.shadowdogs.engine.Loader import Loader
from gdo.shadowdogs.engine.Loot import Loot
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.item.classes.weapon.Fists import Fists
from gdo.table.module_table import module_table
from gdotest.TestUtil import reinstall_module, WebPlug, GDOTestCase, cli_plug, cli_gizmore, all_private_messages


class ShadowdogsTest(GDOTestCase):

    TICKS: int = 0

    def setUp(self):
        super().setUp()
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        clear_cache().gdo_execute()
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
        self.assertIn('received Club_of_Adonis', out, 'gmi does not work.')
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
        self.assertIn('Club_of_Adonis', out, '$sdi 2 does not render.')
        out = cli_plug(gizmore, '$sdeq _of_ado')
        await self.ticker(121)
        out += all_private_messages()
        self.assertIn('Club_of_Adonis as ', out, 'eq does not work.')
        out = cli_plug(gizmore, '$sdq')
        self.assertIn('Weapon: Club_of_Adonis', out, '$sdq does not work.')
        Random.init(9)
        out = cli_plug(gizmore, '$sdgmt gizmore{1} lamer')
        self.assertIn('encounter', out, 'gmt does not work.')
        await self.ticker(260)
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
        out = cli_plug(cli_gizmore(), '$sdat')
        self.assertIn('Str:', out, '$sdattr not working')
        out = cli_plug(cli_gizmore(), '$sdsk')
        self.assertIn('Trading:', out, '$sdskills not working')


    async def test_03_eat(self):
        gizmore = await self.fresh_gizmore()
        out = cli_plug(gizmore, '$sdgmi giz 5xSandwich')
        self.assertIn('receive', out, 'gmi does not work.')
        out = cli_plug(gizmore, '$sds')
        self.assertIn('Food', out, 'not hungry?')
        out = cli_plug(gizmore, '$sduse Sandwich')
        self.assertIn('consumed', out, 'eat sandwich does not work.')
        out = cli_plug(gizmore, '$sduse Sandwich')
        self.assertIn('consumed', out, 'eat sandwich does not work.')
        out = cli_plug(gizmore, '$sduse Sandwich')
        self.assertIn('consumed', out, 'eat sandwich does not work.')
        out = cli_plug(gizmore, '$sduse Sandwich')
        self.assertIn('consumed', out, 'eat sandwich does not work.')
        out = cli_plug(gizmore, '$sduse Sandwich')
        self.assertIn('consumed', out, 'eat sandwich does not work.')
        out = cli_plug(gizmore, '$sduse Sandwich')
        self.assertIn('Item not found', out, 'eat sandwich does not work.')
        out = cli_plug(gizmore, '$sds')
        self.assertIn('Food 200%', out, 'hungry?')

    async def test_09_explore(self):
        gizmore = await self.fresh_gizmore()
        Random.init(1339)
        out = cli_plug(gizmore, '$sdexplore')
        self.assertIn('start to explore', out, 'explore does not work.')
        out = cli_plug(gizmore, '$sdp')
        self.assertIn('exploring Peine', out, 'party does not work.')
        await self.ticker(3333) # half an hour
        out = all_private_messages()
        self.assertIn('new place in Peine', out, 'explore find does not work.')
        out = cli_plug(gizmore, '$sdpl')
        self.assertIn('2 Known Places in Peine', out, 'kp does not work.')
        out = cli_plug(gizmore, '$sden')
        await self.ticker_for()
        out += all_private_messages()
        self.assertIn('enter', out, 'en does not work.')
        out = cli_plug(gizmore, '$sdp')
        self.assertIn('inside', out, 'p does not work.')
        out = cli_plug(gizmore, '$sdleave')
        await self.ticker_for()
        out += all_private_messages()
        self.assertIn('leaving', out, 'leave does not work.')
        out = cli_plug(gizmore, '$sdp')
        self.assertIn('outside', out, 'p does not work.')

    async def test_10_gml(self):
        gizmore = await self.fresh_gizmore()
        out = cli_plug(gizmore, '$sdgml giz in jaw')
        out += all_private_messages()
        self.assertIn('new place', out, '$gml does not work.')

    async def test_11_combat(self):
        gizmore = await self.fresh_gizmore()
        Random.init(1337)
        out = cli_plug(gizmore, '$sdgmt gizmore{1} lamer')
        self.assertIn('encounter', out, 'gmt does not work.')
        await self.ticker(3333) # half an hour
        out += all_private_messages()
        self.assertIn('kills lamer', out, 'combat does not work.')
        out = cli_plug(gizmore, '$sdgmt gizmore{1} noob,noob')
        self.assertIn('encounter', out, 'gmt does not work.')
        await self.ticker(8888) # half an hour
        out += all_private_messages()
        self.assertIn('kills noob', out, 'combat does not work.')

    async def test_13_kw(self):
        gizmore = await self.fresh_gizmore()
        out = cli_plug(gizmore, '$sdsay Laz hi')
        self.assertIn('a new', out, 'say and lazer does not work.')
        out = cli_plug(gizmore, '$sdw')
        self.assertIn('hello', out, 'known words does not work.')

    async def test_15_spells(self):
        gizmore = await self.fresh_gizmore()
        out = cli_plug(gizmore, '$sdgmsp giz calm')
        self.assertIn('hello', out, 'known words does not work.')

    async def test_17_loot(self):
        gizmore = await self.fresh_gizmore()
        giz = Loader.load_user(gizmore)
        ep = await Factory.create_default_npcs(giz.get_location(), 'noob')
        loot = Loot(giz, ep.get_leader())
        Random.init(1339)
        for i in range(100):
            await loot.on_kill()
        out = all_private_messages()
        self.assertGreater(giz.get_nuyen(), 250, "Not enough nuyen looted.")
        self.assertLess(giz.get_nuyen(), 1000, "Not enough nuyen looted.")
        out = cli_plug(gizmore, "$sdny")
        self.assertIn(Shadowdogs.NUYEN, out, '$ny does not work.')
        self.assertFalse(Fists().can_sell(), 'Can sell fists.')
        self.assertFalse(Fists().can_loot(), 'Can loot fists.')

    async def test_20_store(self):
        gizmore = await self.fresh_gizmore()
        giz = Loader.load_user(gizmore)
        out = cli_plug(gizmore, '$sdgml giz inside peine.jawoll')
        out += all_private_messages()
        self.assertIn('a new place', out, '$gml does not work.')
        out = cli_plug(gizmore, '$sdview')
        self.assertIn('Pizza', out, '$gmview does not see pizza.')
        out = cli_plug(gizmore, '$sdvi 1')
        self.assertIn('Pizza is a Consumable', out, '$gmview does not examine pizza.')

    async def test_22_info(self):
        gizmore = await self.fresh_gizmore()
        giz = Loader.load_user(gizmore)
        out = cli_plug(gizmore, '$sdinfo')
        out += all_private_messages()
        self.assertIn('ome sweet', out, '$info does not work.')
        self.assertIn('Fridge', out, '$info does not work#2.')
        out = cli_plug(gizmore, '$sdlook')
        out += all_private_messages()
        self.assertIn('Lazer', out, '$look does not work.')
        self.assertIn('Theo', out, '$look does not work#2.')

    async def test_25_quest(self):
        gizmore = await self.fresh_gizmore()
        out = cli_plug(gizmore, '$sdtalk theo hello')
        self.assertIn('says:', out, '$sdtalk does not work.')
        out = cli_plug(gizmore, '$sdtalk theo hello')
        self.assertIn('sidequest', out, '$sdtalk does not work.')
        out = cli_plug(gizmore, '$sdtalk theo quest')
        self.assertIn('says:', out, '$sdtalk does not work#2.')
        out = cli_plug(gizmore, '$sdtalk theo yes')
        self.assertIn('says:', out, '$sdtalk does not work#3.')
        out = cli_plug(gizmore, '$sdtalk theo yes')
        self.assertIn('says:', out, '$sdtalk does not work#3.')
        out = cli_plug(gizmore, '$sdqus')
        self.assertIn('1-', out, '$sdquests does not work.')
        out = cli_plug(gizmore, '$sdqu 1')
        self.assertIn('Purse:', out, '$sdquest does not work.')
        out = cli_plug(gizmore, '$sdtalk theo purse')
        self.assertIn('says:', out, '$sdtalk does not work#3.')
        out = cli_plug(gizmore, '$sdi')
        self.assertIn('Purse', out, 'have no purse.')
        out = cli_plug(gizmore, '$sdu urse') + all_private_messages()
        self.assertIn('You search the purse...', out, '$sdu purse does not work.')
        out = cli_plug(gizmore, '$sdu urse') + all_private_messages()
        self.assertIn('You search the purse...', out, '$sdu purse does not work#2.')
        out = cli_plug(gizmore, '$sdu urse') + all_private_messages()
        self.assertIn('You search the purse... et voila', out, '$sdu purse does not work#3.')

    async def test_30_goto(self):
        gizmore = await self.fresh_gizmore()
        out = cli_plug(gizmore, '$sdgml giz ins jaw') # move gizmore to Jawoll via gm powers.
        self.assertIn('Jawoll', out, '$sdgml purse does not work.')
        out = cli_plug(gizmore, '$sdgoto Home')
        Random.init(1337)
        await self.ticker(3600)  # an hour
        out = cli_plug(gizmore, '$sdp')
        self.assertIn('Home', out, '$goto does not work.')

    async def test_35_info(self):
        gizmore = await self.fresh_gizmore()
        out = cli_plug(gizmore, '$sdsk')
        self.assertIn('skills', out, '$sk does not work.')
        out = cli_plug(gizmore, '$sdat')
        self.assertIn('attributes', out, '$at does not work.')
        out = cli_plug(gizmore, '$sds')
        self.assertIn('male', out, '$s does not work.')

    async def test_40_lvlup(self):
        gizmore = await self.fresh_gizmore()
        giz = Loader.load_user(gizmore)
        ep = await Factory.create_default_npcs(giz.get_location(), 'noob')
        noob = ep.get_leader()
        from gdo.shadowdogs.engine.Loot import Loot
        for i in range(100):
            await Loot(giz, noob).on_kill_xp()
        out = all_private_messages()
        self.assertIn('karma', out, '$l does not work#1.')
        self.assertIn('level', out, '$l does not work#2.')
        out = cli_plug(gizmore, '$sdl strength')
        self.assertIn('level up', out, '$l does not work.')
        out = cli_plug(gizmore, '$sdl --confirm=1 strength')
        self.assertIn('leveled up', out, '$l does not work.#2')
        out = cli_plug(gizmore, '$sdl --confirm=1 strength')
        self.assertIn('want to level up', out, '$l does not work.#3')

if __name__ == '__main__':
    unittest.main()
