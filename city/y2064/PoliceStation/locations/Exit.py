from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.city.y2064.Peine.locations.police.quest.JackPott import JackPott
from gdo.shadowdogs.locations.Exit import Exit as ExitBase
from gdo.shadowdogs.locations.Location import Location


class Exit(ExitBase):
    def sd_exit_to(self) -> Location:
        return self.world().World2064.Peine.Police

    async def sd_on_entered(self):
        if not JackPott.instance().qv_get('receptioned', ''):
            await self.give_party_kp(self.get_party(), self.world().World2064.PoliceStation.Reception)
            await self.get_party().do(Action.INSIDE, self.world().World2064.PoliceStation.Reception.get_location_key())
            JackPott.instance().qv_set('receptioned', '1')
            await self.mob_attack(self.get_party(), 'peine_cop')
