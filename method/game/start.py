from binascii import crc32

from gdo.base.Render import Mode
from gdo.base.Trans import t
from gdo.base.Util import Random
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.GDT_Race import GDT_Race
from gdo.shadowdogs.city.y2064.World2064 import World2064
from gdo.shadowdogs.engine.Factory import Factory
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.user.GDT_Gender import GDT_Gender


class start(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdstart'

    def sd_requires_player(self) -> bool:
        return False

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_fields(
            GDT_Gender('gender').simple().not_null(),
            GDT_Race('race').not_null(),
        )
        super().gdo_create_form(form)

    async def form_submitted(self):
        if self.get_player():
            return self.err('err_sd_already_started')
        party = Factory.create_party(World2064.Peine.Home)
        race = self.param_val('race')
        player = SD_Player.blank({
            'p_user': self._env_user.get_id(),
            'p_race': race,
            'p_gender': self.param_val('gender'),
            # 'p_party': party.get_id(),
        }).insert()
        party.join_silent(player)
        Shadowdogs.PLAYERS[player.get_id()] = player
        Shadowdogs.USERMAP[player.gdo_val('p_user')] = player
        Shadowdogs.CURRENT_PLAYER = player
        Random.init(crc32(player.get_user().render_name().encode()))
        bonus_bonus = ['p_bod', 'p_str', 'p_int', 'p_wis', 'p_dex', 'p_qui'][Random.mrand(0, 5)]
        player.incb(bonus_bonus, 1).save()
        player.save_values(GDT_Race.BASE[race])
        player.modify_all().heal_full()
        self.msg('msg_sd_started', (
            player.column('p_gender').render(self._env_mode),
            player.column('p_race').render(self._env_mode),))
        await self.character_created(player)
        return self.empty()

    async def character_created(self, player: SD_Player):
        await self.broadcast('msg_sd_new_player', (player.render_name(), player.column('p_gender').render(Mode.render_txt), player.column('p_race').render(Mode.render_txt)))
        await self.send_to_player(player, t('sd_story_1'))
        await self.send_to_player(player, t('sd_story_2'))
        await self.send_to_player(player, t('sd_story_3'))
        await self.give_new_items(player, 'Shorts,TShirt')
        player.inventory.remove_item('Shorts').equip()
        player.inventory.remove_item('TShirt').equip()
        await self.give_kp(player, player.get_party().get_location(), None)
        await self.give_word(player, 'hello', False)
