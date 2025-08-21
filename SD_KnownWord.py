from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Name import GDT_Name
from gdo.core.GDT_Object import GDT_Object
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.GDT_Player import GDT_Player
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.SD_Word import SD_Word


class SD_KnownWord(GDO):

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_Object('kw_word').table(SD_Word.table()).primary(),
            GDT_Player('kw_player').primary(),
            GDT_Created('kw_created'),
        ]

    @classmethod
    def has_word(cls, player: SD_Player, word: str) -> bool:
        return cls.table().select().where(f"kw_word={cls.escape(word)} AND kw_player={player.get_id()}").exec().fetch_val() is not None

    @classmethod
    def give_word(cls, player: SD_Player, word: str):
        obj = SD_Word.get_or_create(word)
        cls.blank({
            'kw_word': obj.get_id(),
            'kw_player': player.get_id(),
        }).insert()
