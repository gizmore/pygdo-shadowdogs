from gdo.base.Result import Result
from gdo.base.ResultArray import ResultArray
from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.engine.MethodSD import MethodSD


class xls(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdls'

    def sd_requires_item_klass(self) -> list[str]:
        return [
            'Deck',
        ]

    def gdo_table_result(self) -> Result:
        return ResultArray(self.get_player().cyberdeck, SD_Item.table())

