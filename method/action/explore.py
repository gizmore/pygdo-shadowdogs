from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodMove import MethodMove


class explore(MethodMove):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdexplore'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdexp'

    async def form_submitted(self):
        pa = self.get_party()
        city = self.get_city()
        await pa.do(Action.EXPLORE, city.get_location_key(), city.get_explore_eta(pa))
        return self.empty()
