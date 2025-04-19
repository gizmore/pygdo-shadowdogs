from gdo.base.Application import Application
from gdo.base.Render import Mode
from gdo.base.Trans import t
from gdo.date.Time import Time
from gdo.form.GDT_Form import GDT_Form
from gdo.form.MethodForm import MethodForm
from gdo.shadowdogs.SD_Party import SD_Party
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.GDT_Race import GDT_Race
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.city.AmBauhof15.AmBauhof15 import AmBauhof15
from gdo.shadowdogs.engine.Factory import Factory
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.user.GDT_Gender import GDT_Gender


class start(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdstart'

    def sd_requires_player(self) -> bool:
        return False

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_Gender('gender').simple().not_null(),
            GDT_Race('race').not_null(),
        )
        super().gdo_create_form(form)

    async def form_submitted(self):
        if self.get_player():
            return self.err('err_sd_already_started')
        party = Factory.create_party(AmBauhof15.Etage2Left)
        player = SD_Player.blank({
            'p_user': self._env_user.get_id(),
            'p_race': self.param_val('race'),
            'p_gender': self.param_val('gender'),
            'p_party': party.get_id(),
        }).insert()
        party.join(player)
        self.msg('msg_sd_started', (
            player.column('p_gender').render(self._env_mode),
            player.column('p_race').render(self._env_mode),))
        await self.character_created(player)
        return self.empty()

    async def character_created(self, player: SD_Player):
        await self.broadcast('msg_sd_new_player', (player.column('p_gender').render(Mode.TXT), player.column('p_race').render(Mode.TXT)))
        await self.send_to_player(player, t('sd_story_1'))
        await self.send_to_player(player, t('sd_story_2'))
        await self.give_items(player, {'Pen': 1, 'Jeans': 1, 'TShirt': 1, 'Shoes': 1})
        await self.give_kp(player, player.get_party().get_location())
