from gdo.shadowdogs.SD_Quest import SD_Quest


class BaM(SD_Quest):

    TIME_SKILL_REQUIRED = 0.5 # time to answer correctly.

    def reward_skill(self) -> dict[str, int]:
        return {
            'p_mat': 1,
        }
