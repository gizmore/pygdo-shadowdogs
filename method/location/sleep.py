from gdo.base.GDT import GDT
from gdo.shadowdogs.engine.MethodSDObstacle import MethodSDObstacle


class sleep(MethodSDObstacle):

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdsl'

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdsleep'

    def sd_is_location_specific(self) -> bool:
        return True

    async def sd_execute(self) -> GDT:
        await self.get_party().do('sleep')
        return self.msg('msg_sd_go_sleeping')
