from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Party import GDO_Party


class Action:

    def execute(self, party: 'GDO_Party'):
        pass
