from gdo.base.Trans import t
from gdo.base.Util import Arrays
from gdo.shadowdogs.SD_Party import SD_Party
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc


class AreaDamage(WithShadowFunc):

    player: SD_Player
    action_text_p: str
    action_text_e: str

    def __init__(self, player: SD_Player, action_text_p: str, action_text_e: str):
        self.player = player
        self.action_text_p = action_text_p
        self.action_text_e = action_text_e

    def cause(self, target: SD_Player, distance: int, damage: int, reduce: float):
        pass

    async def deal_damage(self, target: SD_Player, damage: int):
        return await self.deal_damages([(target, damage)])

    async def deal_damages(self, damages: list[tuple[SD_Player,int]]):
        texts_p = []
        texts_e = []
        for player, damage in damages:
            player.deal_damage(self.player, damage)
            if player.is_alive():
                texts_p.append(t('sd_damaged_p', (player.render_name(), damage, player.gb('p_hp'))))
                texts_e.append(t('sd_damaged_e', (player.render_name(), damage)))
            else:
                texts_p.append(t('sd_killed', (player.render_name(), damage)))
                texts_e.append(t('sd_killed', (player.render_name(), damage)))
        await self.send_to_party(self.player.get_party(), 'msg_sd_area_damage', (self.action_text_p, Arrays.human_join(texts_p)))
        await self.send_to_party(self.player.get_party().get_enemy_party(), 'msg_sd_area_damage', (self.action_text_e, Arrays.human_join(texts_e)))
