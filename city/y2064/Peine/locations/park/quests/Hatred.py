from gdo.shadowdogs.quest.KillQuest import KillQuest


class Hatred(KillQuest):

    KILLS: dict[str, int] = {
        'haider': 10,
    }

    def reward_xp(self) -> int:
        return 10

    def reward(self) -> str|None:
        return '300xNuyen'
