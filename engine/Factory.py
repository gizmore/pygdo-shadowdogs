from gdo.base.Application import Application
from gdo.date.Time import Time
from gdo.shadowdogs.SD_NPC import SD_NPC
from gdo.shadowdogs.SD_Party import SD_Party
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.locations.Location import Location


class Factory(WithShadowFunc):

    @classmethod
    def create_party(cls, location: Location) -> SD_Party:
        party = SD_Party.blank({
            'party_action': 'outside',
            'party_target': location.get_location_key(),
            'party_eta': str(cls.mod_sd().cfg_time()),
        }).insert()
        party.do('inside')
        Shadowdogs.PARTIES[party.get_id] = party
        return party

    @classmethod
    def create_default_npcs(cls, location: Location, *class_names: str):
        specs = []
        for name in class_names:
            specs.append({
                'klass': name,
                'p_race': 'human',
                'p_gender': 'male',
            })
        return cls.create_npcs(location, *specs)

    @classmethod
    def create_npcs(cls, location: Location, *npc_specs: dict[str,int|str]) -> SD_Party:
        party = cls.create_party(location)
        for spec in npc_specs:
            npc = cls.create_npc(party, spec)
            party.join(npc)
        return party

    @classmethod
    def create_npc(cls, party: SD_Party, spec: dict[str,int|str]):
        player = SD_NPC.blank({
            'p_npc_class': spec['klass'],
            'p_npc_name': spec['klass'],
            'p_race': spec['p_race'],
            'p_gender': spec['p_gender'],
            'p_party': party.get_id(),
        }).insert()
        return player
