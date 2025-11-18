from gdo.base.Util import Arrays, Random
from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.WithShadowFunc import WithShadowFunc

from typing import TYPE_CHECKING

from gdo.shadowdogs.engine.Factory import Factory
from gdo.shadowdogs.engine.Shadowdogs import Shadowdogs
from gdo.shadowdogs.engine.WithProbability import WithProbability
from gdo.shadowdogs.item.data.items import items

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Player import SD_Player


class Loot(WithShadowFunc): # <-- t = type[Loot];  t(killer, victim)

    _killer: 'SD_Player'
    _victim: 'SD_Player'

    def __init__(self, killer: 'SD_Player', victim: 'SD_Player'):
        super().__init__()
        self._killer = killer
        self._victim = victim

    async def on_kill(self):
        items = []
        while item := self.loot():
            items.append(item)
        if items:
            await self.give_items(self._killer, items, 'loot', self._victim.render_name())
            lost_string = Arrays.human_join([item.render_name() for item in items])
            await self.send_to_player(self._victim, 'msg_killed_and_lost', (self._killer.render_name(), lost_string))
        await self.on_kill_xp()
        return self

    def loot(self) -> SD_Item|None:
        choices = []
        luck = self._killer.g('p_luc')
        choices.append((self.loot_nuyen, int(Shadowdogs.LOOT_CHANCE_NUYEN + Shadowdogs.LOOT_CHANCE_NUYEN_PER_LUCK * luck)))
        choices.append((self.loot_inventory, int(Shadowdogs.LOOT_CHANCE_INVENTORY + Shadowdogs.LOOT_CHANCE_INVENTORY_PER_LUCK * luck)))
        choices.append((self.loot_equipment, int(Shadowdogs.LOOT_CHANCE_EQUIPMENT + Shadowdogs.LOOT_CHANCE_EQUIPMENT_PER_LUCK * luck)))
        choices.append((self.loot_random, int(Shadowdogs.LOOT_CHANCE_RANDOM + Shadowdogs.LOOT_CHANCE_RANDOM_PER_LUCK * luck)))
        if func := WithProbability.probable_item(choices, Shadowdogs.LOOT_CHANCE_NOTHING):
            return func()
        return None

    def loot_nuyen(self) -> SD_Item|None:
        luck = self._killer.g('p_luc')
        level = self._victim.gb('p_level')
        if self._victim.is_npc():
            nuyen = int(Shadowdogs.LOOT_NUYEN_BASE + (level ** Shadowdogs.LOOT_NUYEN_EXP_LEVEL) + Shadowdogs.LOOT_NUYEN_PER_LUCK * luck)
            nuyen = Random.mrand(Shadowdogs.LOOT_NUYEN_MIN, nuyen)
            return Factory.create_item('Nuyen', nuyen)
        else:
            nuyen = self._victim.get_nuyen()
            if nuyen:
                nuyen = Random.mrand(nuyen // 3, nuyen)
                self._victim.give_nuyen(-nuyen)
                return Factory.create_item('Nuyen', nuyen)
        return None

    def loot_inventory(self) -> SD_Item|None:
        items = self._victim.inventory
        item = Random.list_item(items)
        if not item:
            return None
        count = item.get_count()
        if item.is_equipment():
            count = 1
        count = Random.mrand(1+count//2, count)
        return self._victim.inventory.remove_item(item.render_name(), count)

    def loot_equipment(self) -> SD_Item|None:
        items = []
        for slot_name in GDT_Slot.EQUIPMENT_SLOTS:
            if item := self._victim.get_equipment(slot_name):
                items.append(item)
        item = Random.list_item(items)
        self._victim.save_val(item.get_slot(), None)
        return item


    def loot_random(self) -> SD_Item|None:
        luck = self._killer.g('p_luc')
        itms = []
        for item_name in items.ITEMS.keys():
            item = items.get_item(item_name)
            if item.can_loot():
                itms.append((item_name, item.get_loot_chance(100) + luck * item.get_level()))
        item_name = WithProbability.probable_item(itms)
        if Random.mrand(0, 1000) < Shadowdogs.LOOT_CHANCE_RANDOM_MODIFIER + int(Shadowdogs.LOOT_CHANCE_RANDOM_MODIFIER_PER_LUCK * luck):
            pass # TODO
        count = items.get_item(item_name).get_default_count()
        return Factory.create_item(item_name, count)

    async def on_kill_xp(self):
        level = self._victim.gb('p_level')
        xp = Random.mrand(1, level)
        await self._killer.give_xp(xp)
        return self
