from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodSD import MethodSD


class work(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdwork'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdwk'

    def sd_is_location_specific(self) -> bool:
        return True

    def sd_requires_action(self) -> list[str] | None:
        return [Action.INSIDE]

    async def sd_execute(self):
        return await self.get_location().on_work()
