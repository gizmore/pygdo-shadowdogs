from gdo.form.MethodForm import MethodForm
from gdo.shadowdogs.WithShadowMethod import WithShadowMethod
from gdo.shadowdogs.actions.Action import Action


class MethodSD(WithShadowMethod, MethodForm):

    async def form_submitted(self):
        player = self.get_player()
        if self.sd_method_is_instant():
            gdt = await self.sd_execute()
            if player: player.modify_all()
            return gdt
        if player.get_party().does(Action.FIGHT):
            player.combat_stack().command = self
            return self.empty()
        if player.is_busy():
            await self.send_to_player(player, 'err_sd_player_busy', (player.render_busy(),))
            return self.empty()
        await self.sd_before_execute()
        gdt = await self.sd_execute()
        if player: player.modify_all()
        return gdt

    async def sd_before_execute(self):
        pass

    async def sd_execute(self):
         return self.empty()
