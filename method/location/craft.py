from gdo.base.GDT import GDT
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.item.Item import Item


class craft(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdcraft'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdcr'

    def sd_is_location_specific(self) -> bool:
        return True

    def sd_requires_action(self) -> list[str] | None:
        return [Action.INSIDE]

    def gdo_parameters(self) -> list[GDT]:
        return [
            GDT_ItemArg('item').not_null(),
            GDT_ItemArg('rune').not_null(),
        ]

    def get_item(self) -> Item:
        return self.param_value('item')

    def get_rune(self) -> Item:
        return self.param_value('rune')

    async def sd_execute(self):
        return await self.get_location().on_craft(self.get_player(), self.get_item(), self.get_rune())
