from gdo.core.GDT_RestOfText import GDT_RestOfText
from gdo.shadowdogs.SD_KnownWord import SD_KnownWord
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc


class GDT_Word(WithShadowFunc, GDT_RestOfText):

    def to_value(self, vals: list[str]):
        if vals[0].isdigit():
            return self.from_db(vals[0])
        return vals[0]

    def from_db(self, val: str):
        val = int(val)
        return SD_KnownWord.table().select('k_word').join_object('kw_word').where(f"kw_player={self.get_player()} AND kw_word={val}").limit(1, val-1).first().exec().fetch_val()
