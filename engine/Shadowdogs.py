from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Party import GDO_Party
    from gdo.shadowdogs.GDO_Player import GDO_Player
    from gdo.shadowdogs.GDO_NPC import GDO_NPC


class Shadowdogs:

    PARTIES: list['GDO_Party'] = []
    PLAYERS: list['GDO_Player'] = []
    NPCS: list['GDO_NPC'] = []

    MAX_WEIGHT_PER_STRENGTH = 1000

