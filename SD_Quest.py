import functools

from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Name import GDT_Name
from gdo.core.GDT_UInt import GDT_UInt
from gdo.core.GDT_Virtual import GDT_Virtual
from gdo.date.GDT_Created import GDT_Created
from gdo.shadowdogs.SD_QuestDone import SD_QuestDone


class SD_Quest(GDO):

    @classmethod
    def gdo_table_name(cls) -> str:
        return 'sd_quest'

    @classmethod
    @functools.cache
    def instance(cls, klass: type['SD_Quest']):
        if quest := (cls.table().select().where(f'q_name={GDO.quote(klass.__name__)}').
                     fetch_as(klass).first().exec().fetch_object()):
            return quest
        return klass.blank({
            'q_name': klass.__name__,
        }).insert()

    def gdo_persistent(self) -> bool:
        """
        Prevents the cleansing of the GDO object Process Cache.
        """
        return True

    def gdo_columns(self) -> list[GDT]:
        t = SD_QuestDone.table()
        query_accept = t.select('COUNT(*)').where('qd_accepted IS NOT NULL AND qd_quest=q_id')
        query_denied = t.select('COUNT(*)').where('qd_declined IS NOT NULL AND qd_quest=q_id')
        query_solved = t.select('COUNT(*)').where('qd_success IS NOT NULL AND qd_quest=q_id')
        query_failed = t.select('COUNT(*)').where('qd_failed IS NOT NULL AND qd_quest=q_id')
        return [
            GDT_AutoInc('q_id'),
            GDT_Name('q_name'),
            GDT_Created('q_created'),
            GDT_Virtual(GDT_UInt('q_num_accept')).query(query_accept),
            GDT_Virtual(GDT_UInt('q_num_denied')).query(query_denied),
            GDT_Virtual(GDT_UInt('q_num_solved')).query(query_solved),
            GDT_Virtual(GDT_UInt('q_num_failed')).query(query_failed),
        ]
