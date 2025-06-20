from gdo.base.GDT import GDT
from gdo.shadowdogs.engine.MethodSD import MethodSD


class sleep(MethodSDObstacle):

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdsl'

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdsleep'

    def sd_is_location_specific(self) -> bool:
        return True

    def gdo_execute(self) -> GDT:
        obstacles = self.get_obstacles('sleep')
        pa = self.get_party()
        self.get_party().do('sleep', )
        return self.msg('msg_sd_go_sleeping')

    def get_obstacles(self, param):
        pass