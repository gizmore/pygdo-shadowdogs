from gdo.base.GDT import GDT
from gdo.shadowdogs.engine.MethodSD import MethodSD


class sleep(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdsleep'

    def sd_is_location_specific(self) -> bool:
        return True

    def gdo_execute(self) -> GDT:
        self.get_party().do('sleep')
        return self.msg('msg_sd_go_sleeping')
