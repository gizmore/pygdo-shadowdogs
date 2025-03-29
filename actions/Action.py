from typing import TYPE_CHECKING

from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException

if TYPE_CHECKING:
    from gdo.shadowdogs.GDO_Party import GDO_Party


class Action(WithShadowFunc):

    def execute(self, party: 'GDO_Party'):
        pass

    def sleeping(self, party: 'GDO_Party'):
        pass

    def get_target(self, party: 'GDO_Party'):
        raise ShadowdogsException('err_sd_stub')
