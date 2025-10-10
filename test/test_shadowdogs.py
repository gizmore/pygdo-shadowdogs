import unittest

from gdo.base.Util import Random
from gdo.date.Time import Time
from gdo.shadowdogs.engine.Factory import Factory
from gdo.shadowdogs.engine.Loader import Loader
from gdo.shadowdogs.engine.Loot import Loot
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.item.classes.weapon.Fists import Fists
from gdo.shadowdogs.test.ShadowdogsTestCase import ShadowdogsTestCase
from gdotest.TestUtil import cli_plug, cli_gizmore, all_private_messages


class ShadowdogsTest(ShadowdogsTestCase):

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
        self.assertIn('Club_of_Adonis', out, 'eq does not work.')
        out = cli_plug(gizmore, '$sdq')
        self.assertIn('Club_of_Adonis', out, '$sdq does not work.')
        self.assertIn('Weapon', out, '$sdq does not work.#2')
        Random.init(9)
        out = cli_plug(gizmore, '$sdgmt gizmore{1} lamer')
        self.assertIn('encounter', out, 'gmt does not work.')
        await self.ticker(260)
        out = all_private_messages()
        self.assertIn('kills', out, 'attack does not work.')

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
        out = cli_plug(gizmore, '$sdgmi giz 10xSandwich')
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
        Random.init(31337)
        out = cli_plug(gizmore, '$sdexplore')
        self.assertIn('start to explore', out, 'explore does not work.')
        out = cli_plug(gizmore, '$sdp')
        self.assertIn('exploring Peine', out, 'party does not work.')
        await self.ticker(3333) # half an hour
        out = all_private_messages()
        self.assertIn('new place in Peine', out, 'explore find does not work.')
        out = cli_plug(gizmore, '$sdkp')
        self.assertIn('2 Known Places in Peine', out, 'kp does not work.')
        out = cli_plug(gizmore, '$sden')
        await self.ticker_for()
        out += all_private_messages()
        self.assertIn('enter', out, 'en does not work.')
        out = cli_plug(gizmore, '$sdp')
        self.assertIn('inside', out, 'p does not work.')
        out = cli_plug(gizmore, '$sdx')
        await self.ticker_for()
        out += all_private_messages()
        self.assertIn('leaving', out, 'leave does not work.')
        out = cli_plug(gizmore, '$sdp')
        self.assertIn('outside', out, 'p does not work.')
        out = cli_plug(gizmore, '$sdg home')
        self.assertIn('going', out, 'goto does not work.')
        await self.ticker(3333) # half an hour
        out = all_private_messages()
        self.assertIn('Home', out, 'goto does not work ending.')

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
        out = cli_plug(gizmore, '$sdtalk Laz hi')
        out += cli_plug(gizmore, '$sdtalk Laz hi')
        out += cli_plug(gizmore, '$sdtalk Laz hi')
        self.assertIn('a new', out, 'say and lazer does not work.')
        out = cli_plug(gizmore, '$sdkw')
        self.assertIn('home', out, 'known words does not work.')

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
        out += cli_plug(gizmore, "$sdny")
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
        ep = await Factory.create_default_npcs(giz.get_location(), 'lamer')
        noob = ep.get_leader()
        from gdo.shadowdogs.engine.Loot import Loot
        for i in range(100):
            await Loot(giz, noob).on_kill_xp()
        out = all_private_messages()
        self.assertIn('karma', out, '$l does not work#1.')
        self.assertIn('level', out, '$l does not work#2.')
        out = cli_plug(gizmore, '$sdlev')
        self.assertIn('L', out, '$lev does not work.')
        out = cli_plug(gizmore, '$sdl strength')
        self.assertIn('level up', out, '$l does not work.')
        out = cli_plug(gizmore, '$sdl --confirm=1 strength')
        self.assertIn('leveled up', out, '$l does not work.#2')
        out = cli_plug(gizmore, '$sdl --confirm=1 strength')
        self.assertIn('want to level up', out, '$l does not work.#3')

    async def test_45_cache_and_loader(self):
        gizmore = await self.fresh_gizmore()
        out = cli_plug(gizmore, '$cc')
        self.assertIn('cleared', out, '$cc does not work.')
        out = cli_plug(gizmore, '$sds')
        self.assertIn('male', out, '#s does not work.')
        out = cli_plug(gizmore, '$sds')
        self.assertIn('male', out, '#s does not work.')

    async def test_50_store(self):
        gizmore = await self.fresh_gizmore()
        giz = Loader.load_user(gizmore)
        out = cli_plug(gizmore, '$cc')
        self.assertIn('cleared', out, '$cc does not work.')
        out = cli_plug(gizmore, '$sdgml giz inside Kief')
        self.assertIn('Kief', out, '$gml does not work.')
        out = cli_plug(gizmore, '$sdv')
        self.assertIn('BronzeKnuckles', out, '$v does not work.')
        out = cli_plug(gizmore, '$sdv 2')
        self.assertIn('Shotgun', out, '$v 2 does not work.')
        out = cli_plug(gizmore, '$sdgmi giz 30000xNuyen')
        self.assertIn('30000', out, '$gmi does not work.')
        out = cli_plug(gizmore, '$sdi')
        self.assertIn('30000', out, '$i does not work.')
        out = cli_plug(gizmore, '$sds')
        self.assertIn('30000', out, '$s does not work.')
        out = cli_plug(gizmore, '$sdbuy shot')
        self.assertIn('Shotgun', out, '$buy does not work.')
        out = cli_plug(gizmore, '$sdbuy Ammo12 20')
        self.assertIn('Ammo12g', out, '$buy does not work.#2')
        out = cli_plug(gizmore, '$sdi')
        self.assertIn('Shotgun', out, '$i does not work.')
        out = cli_plug(gizmore, '$sdreload Shotgu')
        await self.ticker_for(gizmore)
        out += all_private_messages()
        self.assertIn('Shotgun', out, '$r does not work.')

    async def test_55_seniors(self):
        gizmore = await self.fresh_gizmore()
        giz = Loader.load_user(gizmore)
        out = cli_plug(gizmore, '$sdsearch')
        self.assertIn('Army', out, '$search does not work.')
        out = cli_plug(gizmore, '$sduse Army')
        self.assertIn('army', out, '$use does not work.')
        out = cli_plug(gizmore, '$sdquests')
        self.assertIn('Civil', out, '$qus does not work.')
        out = cli_plug(gizmore, '$sdquest 1')
        self.assertIn('11', out, '$qu does not work.')
        out = cli_plug(gizmore, '$sdquest Civil')
        self.assertIn('11', out, '$qu does not work.#2')
        out = cli_plug(gizmore, '$sdgml giz inside Senior')
        self.assertIn('Home', out, '$gml does not work.')
        out = cli_plug(gizmore, '$sdtalk nurse hello')
        self.assertIn('Oh hello', out, '$talk does not work.')
        out = cli_plug(gizmore, '$sdtalk nurse work')
        self.assertIn('work', out, '$talk does not work.')
        out = cli_plug(gizmore, '$sdtalk nurse yes')
        self.assertIn('new quest', out, '$talk does not work.')
        out = cli_plug(gizmore, '$sdqus')
        self.assertIn('Civil', out, 'qus does not work.')
        for i in range(11):
            out = cli_plug(gizmore, '$sdwork')
            self.assertIn('one hour', out, 'work does not work.')
            await self.party_ticker_for(gizmore)
            out += all_private_messages()
            self.assertIn('reward', out, 'work does not work.')
        self.assertIn('accomplished', out, 'work does not work.')
        out = cli_plug(gizmore, '$sdny')
        self.assertIn('562', out, 'ny does not work.')

    async def test_57_help(self):
        gizmore = await self.fresh_gizmore()
        out = cli_plug(gizmore, '$sdhelp')
        self.assertIn('know', out, '$help does not work.')
        out = cli_plug(gizmore, '$sdhelp attr')
        self.assertIn('ributes:', out, '$help does not work.#2')

    async def test_58_equip(self):
        gizmore = await self.fresh_gizmore()
        out = cli_plug(gizmore, '$sdsearch')
        self.assertIn('Jeans', out, '$search does not work.')
        out = cli_plug(gizmore, '$sdeq jean')
        self.assertIn('Jeans', out, '$equip does not work.')
        self.assertIn('Shorts', out, '$equip does not work.#2')
        await self.ticker_for(gizmore)
        out = cli_plug(gizmore, '$sdi')
        self.assertNotIn('Jeans', out, '$equip does not work.#3')
        self.assertIn('Shorts', out, '$equip does not work.#4')

    async def test_59_starve(self):
        gizmore = await self.fresh_gizmore()
        await self.ticker(Time.ONE_DAY * 2)
        out = all_private_messages()
        self.assertIn('You are not saturated. 2 damage. 0/10 HP left.', out, 'no starve effect.')



    async def test_60_hack(self):
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


if __name__ == '__main__':
    unittest.main()
