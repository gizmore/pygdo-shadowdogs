from gdo.shadowdogs.city.y2064.Peine.locations.bank.Clerk import Clerk
from gdo.shadowdogs.locations.Bank import Bank as BaseBank
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class Bank(BaseBank):

    NPCS: 'list[type[TalkingNPC]]' = [
        Clerk,
    ]
