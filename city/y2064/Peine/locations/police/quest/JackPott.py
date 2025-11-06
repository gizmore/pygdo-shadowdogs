from gdo.shadowdogs.SD_Quest import SD_Quest


class JackPott(SD_Quest):

    def reward(self) -> str | None:
        return '2xCocaine,2xExtasy'

    def reward_xp(self) -> int:
        return 20
    