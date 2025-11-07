from gdo.base.GDO import GDO
from gdo.base.ResultArray import ResultArray
from gdo.base.Result import Result
from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.WithShadowMethod import WithShadowMethod
from gdo.table.MethodTable import MethodTable


class inventory(WithShadowMethod, MethodTable):
    """
    This is enough to render a searchable paginated inventory in web, cli, chats and where-not
    """
    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdinventory'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdi'

    def gdo_table(self) -> GDO:
        return SD_Item.table()

    def gdo_table_result(self) -> Result:
        return ResultArray(self.get_player().inventory, SD_Item.table())
