from gdo.base.Trans import t
from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.SD_Party import SD_Party
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException
from gdo.shadowdogs.item.data.items import items
from gdo.shadowdogs.item.data.mapping import mapping
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.npcs.npcs import npcs


class Factory(WithShadowFunc):

    #########
    # Party #
    #########

    @classmethod
    def create_party(cls, location: Location) -> SD_Party:
        party = SD_Party.blank({
            'party_action': 'inside',
            'party_target': location.get_location_key(),
            'party_eta': '0',
            'party_last_action': 'outside',
            'party_last_target': location.get_location_key(),
            'party_last_eta': '0',
        }).insert()
        Shadowdogs.PARTIES[party.get_id()] = party
        return party

    ########
    # NPCs #
    ########

    @classmethod
    async def create_default_npcs(cls, location: Location, *class_names: str) -> SD_Party:
        specs = []
        for name in class_names:
            spec = {
                'type': name,
                'p_race': 'human',
                'p_gender': 'male',
                'p_npc_name': name,
            }
            spec.update(npcs.NPCS.get(name))
            specs.append(spec)
        return await cls.create_npcs(location, *specs)

    @classmethod
    async def create_npcs(cls, location: Location, *npc_specs: dict[str,int|str]) -> SD_Party:
        party = cls.create_party(location)
        for spec in npc_specs:
            npc = cls.create_npc(party, spec)
            party.join_silent(npc)
        return party

    @classmethod
    def create_npc(cls, party: SD_Party, spec: dict[str,int|str]) -> SD_Player:
        klass = npcs.NPCS[spec['type']]['klass']
        player = klass.blank({
            'p_npc_class': klass.fqcn(),
            'p_npc_name': spec['type'],
            'p_race': spec['p_race'],
            'p_gender': spec['p_gender'],
            'p_party': party.get_id(),
        }).insert()
        for item_name in spec.get('eq', []):
            item = Factory.create_item_gmi(item_name, player, True)
            player.save_val(item.get_slot(), item.get_id())
        return player.modify_all().heal_full()

    #########
    # Items #
    #########

    @classmethod
    def create_item_gmi(cls, full_item_name: str, player: SD_Player=None, equipped: bool=False):
        """
        like 2xClub_of_adonis,osiris
        """
        count = 1
        if full_item_name[0].isdigit():
            count, full_item_name = full_item_name.split('x', 1)
        data = full_item_name.split(Shadowdogs.MODIFIER_SEPERATOR)
        mods = data[1] if len(data) > 1 else None
        key = data[0].lower()
        firsts = []
        candidates = []
        for k in items.ITEMS.keys():
            name = t(k).lower()
            if name == key:
                candidates = [k]
                break
            if name.startswith(key):
                firsts.append(k)
                candidates.append(k)
            elif key in name:
                candidates.append(k)
        if len(firsts) == 1:
            candidates = firsts
        if not candidates:
            raise ShadowdogsException('err_sd_invalid_item_name', (t(full_item_name),))
        if not mapping.is_valid(mods):
            raise ShadowdogsException('err_sd_invalid_modifier', (mods,))
        if len(candidates) > 1:
            raise ShadowdogsException('err_sd_ambiguous', (len(candidates), ", ".join([t(c) for c in candidates[:5]]),))
        player_id = player.get_id() if player else None
        return cls.create_item(candidates[0], count, mods, player_id, equipped)

    @classmethod
    def create_item(cls, item_name: str, count: int=1, mods: str=None, player_id: str=None, equipped: bool=False):
        item = items.get_item(item_name)
        return item.set_vals({
            'item_owner': player_id or '1',
            'item_slot': item.get_slot() if equipped else GDT_Slot.NEXUS,
            'item_name': item_name,
            'item_mods': mods,
            'item_count': str(count),
        }).validated().insert()
