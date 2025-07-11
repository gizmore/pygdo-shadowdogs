from gdo.shadowdogs.SD_NPC import SD_NPC


class TalkingNPC(SD_NPC):

    def get_name(self):
        return self.__class__.__name__
