from typing import TYPE_CHECKING

from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.ShadowdogsException import ShadowdogsException

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Party import SD_Party


class Action(WithShadowFunc):

    async def execute(self, party: 'SD_Party'):
        pass

    async def sleeping(self, party: 'SD_Party'):
        pass

    def get_target(self, party: 'SD_Party'):
        raise ShadowdogsException('err_sd_stub')
