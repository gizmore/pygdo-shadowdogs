from gdo.core.GDO_Permission import GDO_Permission
from gdo.core.GDT_Repeat import GDT_Repeat
from gdo.core.GDT_RestOfText import GDT_RestOfText
from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.Factory import Factory
from gdo.shadowdogs.engine.MethodSD import MethodSD


class gmt(MethodSD):
    """
    Create a target party with npcs.
    """

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdgmt'

    def gdo_user_permission(self) -> str | None:
        return GDO_Permission.ADMIN

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_fields(
            GDT_Player('target').online().not_null(),
            GDT_RestOfText('npcs').not_null(),
        )
        super().gdo_create_form(form)

    def get_target(self) -> SD_Player:
        return self.param_value('target')

    async def form_submitted(self):
        player = self.get_target()
        npc_names = self.param_value('npcs').split(',')
        party = player.get_party()
        if party.does(Action.FIGHT, Action.TALK, Action.HACK):
            return self.err('err_sd_gmt_party_busy')
        enemies = await Factory.create_default_npcs(party.get_location(), *npc_names)
        await party.fight(enemies)
        return self.empty()
