from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc


class sleep(WithShadowFunc, Method):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdsleep'

    def sd_is_location_specific(self) -> bool:
        return True

    def gdo_execute(self) -> GDT:
        self.get_party().do('sleep')
        return self.msg('msg_sd_go_sleeping')
