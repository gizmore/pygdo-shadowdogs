from typing import Iterator

from gdo.core.GDO_Channel import GDO_Channel
from gdo.core.GDO_User import GDO_User
from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.SD_NPC import SD_NPC
from gdo.shadowdogs.SD_Party import SD_Party
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.Factory import Factory
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.engine.WorldBase import WorldBase
from gdo.shadowdogs.locations.City import City
from gdo.shadowdogs.locations.Location import Location
from gdo.shadowdogs.method.game.start import start


class Loader(WithShadowFunc):

    @classmethod
    def cleanup(cls):
        result = SD_Party.table().select("sd_party.*, (SELECT COUNT(*) FROM sd_player WHERE p_party=party_id) num_members").having('num_members=0').nocache().exec()
        for party in result:
            party.delete()

    @classmethod
    def get_location_npc_classes(cls) -> Iterator[tuple[WorldBase,City,Location,type[SD_NPC]]]:
        for world in cls.world().WORLDS.values():
            for city in world.CITIES.values():
                for location in city.LOCATIONS:
                    for klass in location.NPCS:
                        yield world, city, location, klass

    @classmethod
    def load_npcs(cls):
        for world, city, location, klass in cls.get_location_npc_classes():
            if not (player := SD_Player.table().select().where(f"p_npc_class='{klass.fqcn()}'").exec().fetch_object()):
                npc = klass.blank()
                npc.set_val('p_npc_class', klass.fqcn())
                npc.set_val('p_npc_name', klass.__name__)
                npc.save()
                party = Factory.create_party(location)
                party.join_silent(npc)
                player = npc
            else:
                player.get_party().join_silent(player)
            location.NPC_INSTANCES.append(player)
            Shadowdogs.LOCATION_NPCS[player.fqcn()] = player
            Shadowdogs.PARTIES[player.gdo_val('p_party')] = player.get_party()

    @classmethod
    def init_npc_classes(cls):
        from gdo.shadowdogs.GDT_NPCClass import GDT_NPCClass
        for world, city, location, klass in cls.get_location_npc_classes():
            GDT_NPCClass.TALKING_NPCS[klass.fqcn()] = klass

    @classmethod
    def load_parties(cls):
        parties = (SD_Party.table().select().
                   where("party_action IN ('goto', 'explore', 'talk', 'sleep', 'travel', 'fight', 'hack')").
                   exec()) #.fetch_all())
        for party in parties:
            cls.load_party(party)

    @classmethod
    def load_party(cls, party: SD_Party):
        if party.get_id() not in Shadowdogs.PARTIES:
            pids = SD_Player.table().select().order('p_created DESC').where(f'p_party={party.get_id()}').exec(False).fetch_column()
            for pid in pids:
                if pid not in Shadowdogs.PLAYERS:
                    player = SD_Player.table().get_by_aid(pid)
                    Shadowdogs.CURRENT_PLAYER = player
                    Shadowdogs.PLAYERS[player.get_id()] = player
                    Shadowdogs.USERMAP[player.gdo_val('p_user')] = player
                    cls.load_items(player)
                    party.members.append(player.modify_all())
                    party.with_fresh_positions()
            Shadowdogs.PARTIES[party.get_id()] = party
        return party

    @classmethod
    def load_items(cls, player: SD_Player):
        player.inventory.clear()
        items = SD_Item.table().select().where(f"item_owner={player.get_id()} AND item_slot='inventory'").exec()
        for item in items:
            player.inventory.add_item(item)

    @classmethod
    def load_user(cls, user: GDO_User) -> SD_Player | None:
        if party_id := SD_Player.table().select('p_party').where(f'p_user={user.get_id()}').first().exec().fetch_val():
            if party_id not in Shadowdogs.PARTIES:
                cls.load_party(SD_Party.table().get_by_aid(party_id))
            return Shadowdogs.USERMAP[user.get_id()]
        return None

    @classmethod
    def channels_with_shadowlamb(cls) -> list[GDO_Channel]:
        back = []
        channels = GDO_Channel.with_setting(start(), 'enabled', '1', '0')
        for channel in channels:
            if channel.is_online():
                back.append(channel)
        return back
