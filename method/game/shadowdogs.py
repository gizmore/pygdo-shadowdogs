from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_Template import GDT_Template
from gdo.core.GDT_UserType import GDT_UserType
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.method.game.start import start
from gdo.shadowdogs.method.info.inventory import inventory


class shadowdogs(WithShadowFunc, Method):

    def gdo_user_type(self) -> str | None:
        return GDT_UserType.MEMBER + "," + GDT_UserType.GUEST

    def gdo_execute(self) -> GDT:
        user = GDO_User.current()

        player = SD_Player.table().select().where(f'p_user={user.get_id()}').first().exec().fetch_object()

        if not player:
            return GDT_Template().template('shadowdogs', 'sds.html', {
                'start': start().env_copy(self),
            })

        return GDT_Template().template('shadowdogs', 'sd.html', {
            'inventory': inventory().env_copy(self),
        })
