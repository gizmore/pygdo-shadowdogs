from gdo.base.Application import Application
from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.date.GDT_Created import GDT_Created
from gdo.date.GDT_Timestamp import GDT_Timestamp
from gdo.date.Time import Time
from gdo.shadowdogs.GDT_Action import GDT_Action
from gdo.shadowdogs.GDT_Target import GDT_Target

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Player import GDO_Player
    from gdo.shadowdogs.GDO_Member import GDO_Member


class GDO_Party(GDO):

    members: list['GDO_Player']

    __slots__ = (
        'members'
    )

    def __init__(self):
        super().__init__()
        self.members = []

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('party_id'),
            GDT_Action('party_action').not_null(),
            GDT_Target('party_target').not_null(),
            GDT_Timestamp('party_eta').not_null(),
            GDT_Action('party_last_action'),
            GDT_Target('party_last_target'),
            GDT_Timestamp('party_last_eta'),
            GDT_Created('party_created'),
        ]

    def do(self, action: str, target: str = None, eta: int = None):
        self.set_val('party_last_action', self.gdo_val('party_action'))
        self.set_val('party_last_target', self.gdo_val('party_target'))
        self.set_val('party_last_eta', self.gdo_val('party_eta')) # compute remaining seconds
        self.set_val('party_action', action)
        self.set_val('party_target', target if target else self.gdo_val('party_target'))
        self.set_val('party_eta', Time.get_date(Application.TIME + eta) if eta else None)
        return self.save()

    def resume(self):
        return self.do(
            self.gdo_val('party_last_action'),
            self.gdo_val('party_last_target'),
            self.gdo_val('party_last_eta'),
        )

    def join(self, player: 'GDO_Player'):
        from gdo.shadowdogs.GDO_Member import GDO_Member
        self.members.append(GDO_Member.blank({
            'm_party': self.get_id(),
            'm_player': player.get_id(),
        }).insert())
        return self
