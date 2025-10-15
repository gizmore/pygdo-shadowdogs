from gdo.base.Util import Arrays
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class DeliveryQuest(SD_Quest):

    ITEM_NAMES = ""
    TARGET_NPC: type[TalkingNPC] = None

    ###########
    # Deliver #
    ###########

    def deliver_items(self) -> bool:
        delivered = True
        for item_name in self.ITEM_NAMES.split(','):
            if not self.deliver_item(item_name):
                delivered = False
        return delivered

    def deliver_item(self, item_name: str) -> bool:
        need = 1
        if item_name[0].isdigit():
            count, item_name = item_name.split(',')
            need = int(count)
        delivered = int(self.qv_get(item_name, '0'))
        need -= delivered
        if need <= 0:
            return True
        p = self.get_player()
        if item := p.inventory.remove_item(item_name, need):
            delivered += item.get_count()
            need -= item.get_count()
            item.delete()
        return need <= 0

    ##########
    # Render #
    ##########

    def render_descr_items(self):
        out = []
        for item_name in self.ITEM_NAMES.split(','):
            need = 1
            if item_name[0].isdigit():
                count, item_name = item_name.split(',', 1)
                need = int(count)
            delivered = int(self.qv_get(item_name, '0'))
            out.append(f"{delivered}/{need} {self.t(item_name)}")
        return Arrays.human_join(out)

    def render_descr(self) -> str:
        return self.t(f'sdqd_{self.__class__.__name__.lower()}', (self.render_descr_items(),))
