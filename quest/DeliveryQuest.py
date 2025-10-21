from gdo.base.Util import Arrays
from gdo.shadowdogs.SD_Quest import SD_Quest
from gdo.shadowdogs.item.Item import Item
from gdo.shadowdogs.npcs.TalkingNPC import TalkingNPC


class DeliveryQuest(SD_Quest):

    ITEM_NAMES = ""
    TARGET_NPC: type[TalkingNPC] = None

    def get_npc(self) -> TalkingNPC:
        return self.TARGET_NPC.instance()

    ########
    # Give #
    ########
    async def on_give(self, item: Item) -> bool:
        total_need = self.get_total_need_count(item)
        have = int(self.qv_get(item.render_name_wc(), '0'))
        need = total_need - have
        if need <= 0:
            return False
        await self.get_npc().say('sdqs_given_thx', (item.render_name(),))
        if self.deliver_items(item):
            await self.accomplished()
        return False

    def get_total_need_count(self, item: Item) -> int:
        for item_name in self.ITEM_NAMES.split(','):
            need = 1
            if item_name[0].isdigit():
                need, item_name = item_name.split('x')
            if item_name == item.get_item_name():
                return int(need)
        return 0

    ###########
    # Deliver #
    ###########

    def deliver_items(self, item: Item) -> bool:
        delivered = True
        for item_name in self.ITEM_NAMES.split(','):
            if not self.deliver_item(item_name, item):
                delivered = False
        return delivered

    def deliver_item(self, item_name: str, item: Item) -> bool:
        need = 1
        if item_name[0].isdigit():
            count, item_name = item_name.split('x')
            need = int(count)
        delivered = int(self.qv_get(item_name, '0'))
        need -= delivered
        if need <= 0:
            return True
        p = self.get_player()
        # if item := p.inventory.remove_item(item.render_name_wc(), need):
        delivered += item.get_count()
        need -= item.get_count()
        item.delete()
        self.qv_set(item_name, str(delivered))
        return need <= 0

    ##########
    # Render #
    ##########

    def render_descr_items(self):
        out = []
        for item_name in self.ITEM_NAMES.split(','):
            need = 1
            if item_name[0].isdigit():
                count, item_name = item_name.split('x', 1)
                need = int(count)
            delivered = int(self.qv_get(item_name, '0'))
            out.append(f"{delivered}/{need} {self.t(item_name)}")
        return Arrays.human_join(out)

    def render_descr(self) -> str:
        return self.t(f'sdqd_{self.__class__.__name__.lower()}', (self.render_descr_items(),))
