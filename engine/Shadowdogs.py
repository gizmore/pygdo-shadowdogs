from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Party import GDO_Party
    from gdo.shadowdogs.GDO_Player import GDO_Player
    from gdo.shadowdogs.GDO_NPC import GDO_NPC


class Shadowdogs:

    PARTIES: dict[str,'GDO_Party'] = {}
    PLAYERS: dict[str,'GDO_Player'] = {}
    NPCS: dict[str,'GDO_NPC'] = {}

    MAX_WEIGHT_PER_STRENGTH = 1000

