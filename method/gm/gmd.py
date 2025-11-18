from asyncio import iscoroutine

from gdo.base.Application import Application
from gdo.base.GDT import GDT
from gdo.base.Message import Message
from gdo.core.GDO_Permission import GDO_Permission
from gdo.core.GDT_RestOfText import GDT_RestOfText
from gdo.core.method.launch import launch
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.GDT_TargetArg import GDT_TargetArg
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.MethodSD import MethodSD


class gmd(MethodSD):
    """
    GM Do - somthing as another player.
    """

    @classmethod
    def gdo_trigger(cls) -> str:
        return "sdgmd"

    def gdo_user_permission(self) -> str | None:
        return GDO_Permission.ADMIN

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_fields(
            GDT_Player('player').not_null(),
            GDT_RestOfText('command').not_null(),
        )
        super().gdo_create_form(form)

    def get_target(self) -> SD_Player:
        return self.param_value('player')

    async def gdo_execute(self) -> GDT:
        player = self.get_target()
        user = player.get_user()
        command = self.param_val('command')
        msg = (Message(command, self._env_mode).
               env_user(user, True).
               env_server(self._env_server).
               env_channel(self._env_channel))
        gdt = msg.execute()
        while iscoroutine(gdt):
            gdt = await gdt
        if gdt: await self.send_to_player(self.get_player(), '%s', (gdt.render(self._env_mode),))
        return self.empty()
