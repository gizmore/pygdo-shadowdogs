from gdo.base.Application import Application
from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.date.GDT_Created import GDT_Created
from gdo.date.GDT_Timestamp import GDT_Timestamp
from gdo.date.Time import Time
from gdo.shadowdogs.GDT_Action import GDT_Action
from gdo.shadowdogs.GDT_Target import GDT_Target


class GDO_Party(GDO):

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

    def do(self, action: str, target: str, eta: int):
        self.set_val('party_last_action', self.gdo_val('party_action'))
        self.set_val('party_last_target', self.gdo_val('party_target'))
        self.set_val('party_last_eta', self.gdo_val('party_eta'))
        self.set_val('party_action', action)
        self.set_val('party_target', target)
        self.set_val('party_eta', Time.get_date(Application.TIME + eta))
        self.save()
