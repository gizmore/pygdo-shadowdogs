from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_World import GDT_World
from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.engine.WorldBase import WorldBase
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class world(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return "sdworld"

    @classmethod
    def gdo_trig(cls) -> str:
        return "sdwo"

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_World('year').not_null().default_current(),
        )
        super().gdo_create_form(form)

    def get_world(self) -> WorldBase:
        return self.param_value('year')

    async def sd_execute(self):
        world = self.get_world()
        doing = {
            Action.INSIDE: 0,
            Action.OUTSIDE: 0,
            Action.FIGHT: 0,
            Action.TALK: 0,
            Action.EXPLORE: 0,
            Action.SLEEP: 0,
            Action.TRAVEL: 0,
            Action.GOTO: 0,
            Action.HACK: 0,
        }
        parties = 0
        humans = 0
        talking = 0
        mobs = 0
        players = 0
        nuyen = 0
        for party in world.get_parties():
            doing[party.get_action_name()] += len(party.members)
            players += len(party.members)
            parties += 1
            for member in party.members:
                if not member.is_npc():
                    humans += 1
                    nuyen += member.get_nuyen() + member.get_bank_nuyen()
                elif isinstance(member, TalkingNPC):
                    talking += 1
                else:
                    mobs += 1
        locations = 0
        for city in world.CITIES.values():
            locations += len(city.LOCATIONS)
        self.msg('msg_sd_world',
                  (world.render_name(), len(world.CITIES), locations,
                         parties,
                         doing[Action.EXPLORE] + doing[Action.GOTO],
                         doing[Action.TALK],
                         doing[Action.FIGHT],
                         doing[Action.INSIDE] + doing[Action.OUTSIDE] + doing[Action.SLEEP],
                         doing[Action.HACK],
                         doing[Action.TRAVEL],
                         players,
                         talking,
                         humans,
                         mobs,
                         nuyen))
        return self.empty()
