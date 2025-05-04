from gdo.base.Util import html
from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.SD_Party import SD_Party
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException
from gdo.shadowdogs.engine.World import World
from gdo.shadowdogs.item.data.items import items
from gdo.shadowdogs.item.data.mapping import mapping
from gdo.shadowdogs.locations.Location import Location


class Factory(WithShadowFunc):

    @classmethod
    async def create_party(cls, location: Location) -> SD_Party:
        party = SD_Party.blank({
            'party_action': 'outside',
            'party_target': location.get_location_key(),
            'party_eta': str(cls.mod_sd().cfg_time()),
        }).insert()
        await party.do('inside')
        Shadowdogs.PARTIES[party.get_id()] = party
        return party

    ########
    # NPCs #
    ########

    @classmethod
    async def create_default_npcs(cls, location: Location, *class_names: str):
        specs = []
        for name in class_names:
            specs.append({
                'klass': name,
                'p_race': 'human',
                'p_gender': 'male',
            })
        return await cls.create_npcs(location, *specs)

    @classmethod
    async def create_npcs(cls, location: Location, *npc_specs: dict[str,int|str]) -> SD_Party:
        party = await cls.create_party(location)
        for spec in npc_specs:
            npc = cls.create_npc(party, spec)
            await party.join(npc)
        return party

    @classmethod
    def create_npc(cls, party: SD_Party, spec: dict[str,int|str]):
        player = World.get_npc_class(spec['klass']).blank({
            'p_npc_class': spec['klass'],
            'p_npc_name': spec['klass'],
            'p_race': spec['p_race'],
            'p_gender': spec['p_gender'],
            'p_party': party.get_id(),
        }).insert()
        return player

    #########
    # Items #
    #########

    @classmethod
    def create_item_gmi(cls, full_item_name: str):
        """
        like 2xClub_of_adonis,osiris
        """
        count = 1
        if full_item_name[0].isdigit():
            count, full_item_name = full_item_name.split('x', 1)
        data = full_item_name.split(Shadowdogs.MODIFIER_SEPERATOR)
        mods = data[1] if len(data) > 1 else None
        key = data[0]
        found = False
        for key in items.ITEMS.keys():
            if key.lower() == data[0].lower():
                found = True
                break
        if not found:
            raise ShadowdogsException('err_sd_invalid_item_name', (html(data[0]),))
        if not mapping.is_valid(mods):
            raise ShadowdogsException('err_sd_invalid_modifier', (mods,))

        return cls.create_item(key, count, mods)

    @classmethod
    def create_item(cls, item_name: str, count: int=1, mods: str=None):
        return SD_Item.blank({
            'item_owner': '1',
            'item_slot': 'nexus',
            'item_name': item_name,
            'item_mods': mods,
            'item_count': str(count),
        }).validated().insert()
