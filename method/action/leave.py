from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodSD import MethodSD


class leave(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdleave'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdle'

    def sd_execute(self):
        self.get_party().do(Action.OUTSIDE)
        return self.empty()
