import os

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdo.core.method.clear_cache import clear_cache
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.engine.WorldBase import WorldBase
from gdo.shadowdogs.item.classes.Equipment import Equipment
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.method.info.world import world
from gdo.table.module_table import module_table
from gdotest.TestUtil import GDOTestCase, reinstall_module, WebPlug, cli_gizmore, cli_plug


class ShadowdogsTestCase(WithShadowFunc, GDOTestCase):

    async def asyncSetUp(self):
        await super().asyncSetUp()
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        loader = ModuleLoader.instance()
        loader.load_modules_db(True)
        reinstall_module('shadowdogs')
        await clear_cache().gdo_execute()
        WebPlug.COOKIES = {}
        Application.init_cli()
        loader.init_modules(True, True)
        loader.init_cli()
        module_table.instance().save_config_val('table_ipp', '10')

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
            out = cli_plug(gizmore, '$sdeq shoe')
            await self.ticker_for()
            out = cli_plug(gizmore, '$sdeq jean')
            await self.ticker_for()
        Shadowdogs.CURRENT_PLAYER = self.sd_gizmore()
        return gizmore

    async def power_gizmore(self, level: int, lvlups: str, equipment: str):
        giz = await self.fresh_gizmore()
        gizmore = self.sd_gizmore()
        while gizmore.gb('p_level') < level:
            await gizmore.give_xp(3)
        for lvlup in lvlups.split(','):
            out = cli_plug(giz, f'$sdlvlup --confirm=1 {lvlup}')
        for item_name in equipment.split(','):
            item = self.factory().create_item_gmi(item_name, gizmore, False)
            if isinstance(item, Equipment):
                item.equip()
        return gizmore.modify_all().heal_full()

    def all_locations(self):
        w = self.world()
        yield from self.all_year_locations(w.World2064)
        yield from self.all_year_locations(w.World2077)
        yield from self.all_year_locations(w.World2088)

    def all_year_locations(self, world: WorldBase):
        for city in world.CITIES.values():
            yield from self.all_city_locations(city)

    def all_city_locations(self, city: City):
        yield from city.LOCATIONS