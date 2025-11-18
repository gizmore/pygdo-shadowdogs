from gdo.shadowdogs.city.y2064.Peine.locations.police.quest.JackPott import JackPott
from gdo.shadowdogs.locations.Exit import Entry
from gdo.shadowdogs.locations.Location import Location


class Police(Entry):

    def sd_exit_to(self) -> Location:
        return self.world().World2064.PoliceStation.Exit

    async def on_entered(self):
        if JackPott.instance().is_in_quest():
            await super().on_entered()
        else:
            await self.send_to_party(self.get_party(), 'sdqs_police_no_time')
