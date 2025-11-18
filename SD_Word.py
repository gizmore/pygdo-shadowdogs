from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Name import GDT_Name


class SD_Word(GDO):

    def gdo_persistent(self) -> bool:
        return True

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('w_id'),
            GDT_Name('w_name'),
        ]

    @classmethod
    def get_or_create(cls, word: str):
        if (obj := cls.table().get_by('w_name', word)) is None:
            obj = cls.blank({
                'w_name': word,
            }).insert()
        return obj
