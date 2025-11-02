from gdo.shadowdogs.quest.KillQuest import KillQuest


class Baptism(KillQuest):

    KILLS: dict[str, int] = {
        'lamer': 6,
    }

    def reward_xp(self) -> int:
        return 6

    def reward(self) -> str|None:
        return '50xNuyen'
