from gdo.core.GDO_Permission import GDO_Permission
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.stat.Karma import Karma


class gmk(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdgmk'

    def gdo_user_permission(self) -> str | None:
        return GDO_Permission.ADMIN

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_fields(
            GDT_Player('player').humans().online().not_null(),
            Karma('amount').not_null().positional(),
        )
        super().gdo_create_form(form)

    def get_target_player(self) -> SD_Player:
        return self.param_value('player')

    async def sd_execute(self):
        player = self.get_target_player()
        amount = self.param_value('amount')
        player.incb('p_karma', amount).save()
        await self.send_to_player(player, 'msg_sd_gmk_you', (self.get_player().render_name(), amount, player.gb('p_karma')))
        return self.reply('msg_sd_gmk', (player.render_name(), amount, player.gb('p_karma')))
