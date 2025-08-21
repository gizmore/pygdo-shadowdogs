from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class Loot(WithShadowFunc):
    """

    """

    @classmethod
    def on_killed(cls, killer: 'SD_Player', victim: 'SD_Player') -> list[SD_Item]:

        if killer.is_npc():
            if victim.is_npc():
                return []
            else:
                return cls.on_npc_killed_human(killer, victim)
        else:
            if victim.is_npc():
                return []
            else:
                return cls.on_npc_killed_human(killer, victim)


    @classmethod
    def on_npc_killed_human(cls, killer: 'SD_Player', victim: 'SD_Player') -> list[SD_Item]:
        return []

    @classmethod
    def on_human_killed_human(cls, killer: 'SD_Player', victim: 'SD_Player') -> list[SD_Item]:
        return []

    @classmethod
    def on_human_killed_npc(cls, killer: 'SD_Player', victim: 'SD_Player') -> list[SD_Item]:
        return []
