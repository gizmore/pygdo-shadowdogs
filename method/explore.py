from gdo.base.Application import Application
from gdo.base.Render import Mode
from gdo.base.Trans import t
from gdo.date.Time import Time
from gdo.form.GDT_Form import GDT_Form
from gdo.form.MethodForm import MethodForm
from gdo.shadowdogs.SD_Party import SD_Party
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.GDT_City import GDT_City
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.MethodSD import MethodSD


class explore(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdexplore'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdexp'

    # def gdo_create_form(self, form: GDT_Form) -> None:
    #     form.add_field(
    #         GDT_City('area').known().not_null(),
    #     )
    #     super().gdo_create_form(form)

    def form_submitted(self):
        if self.get_player():
            return self.err('err_sd_already_started')
        party = SD_Party.blank({
            'party_action': 'sleep',
            'party_target': 'AmBauhof15.Etage2Left',
            'party_eta': Time.get_date(Application.TIME + 10),
        }).insert()
        party.do('inside')
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
        self.character_created(player)
        return self.empty()

    def character_created(self, player: SD_Player):
        self.broadcast('msg_sd_new_player', (player.column('p_gender').render(Mode.TXT), player.column('p_race').render(Mode.TXT)))
        self.send_to_player(player, t('sd_story_1'))
        self.send_to_player(player, t('sd_story_2'))
        self.give_items(player, {'Pen':1, 'Jeans':1, 'TShirt':1, 'Shoes':1})
