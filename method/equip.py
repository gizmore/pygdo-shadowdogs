from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_Slot import GDT_Slot
from gdo.shadowdogs.SD_Item import SD_Item
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.SD_Player import SD_Player
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.item.Item import Item


class equip(MethodSD):

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdeq'

    def sd_combat_seconds(self) -> int:
        return self.get_item().get_equip_time()

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(
            GDT_ItemArg('item').gdo(self.get_player()).inventory().not_null(),
        )
        super().gdo_create_form(form)

    def get_SD_Item(self) -> SD_Item:
        return self.param_value('item')

    def get_item(self) -> Item:
        return self.get_SD_Item().itm()

    def form_submitted(self):
        player = self.get_player()
        item = self.get_SD_Item()
        itm = item.itm()
        time = 0
        key = 'msg_sd_item_equip'
        args = []
        if old_item := player.get_equip(itm.get_slot()):
            self.unequip(player, itm.get_slot())
            key = 'msg_sd_item_re_equip'
            time += old_item.itm().get_unequip_time()
            args.append(old_item.render_name())
        self.equip(player, item)
        args.append(item.render_name())
        args.append(itm.get_slot())
        time += itm.get_equip_time()
        args.append(player.busy(time))
        return self.msg(key, tuple(args))

    def equip(self, player: SD_Player, item: SD_Item) -> bool:
        player.inventory.remove(item)
        slot = item.itm().get_slot()
        item.save_val('item_slot', slot)
        player.save_val(slot, item.get_id())
        return True

    def unequip(self, player: SD_Player, item_slot: str) -> bool:
        if item := player.get_equip(item_slot):
            player.inventory.append(item)
            item.save_val('item_slot', GDT_Slot.INVENTORY)
            player.save_val(item_slot, None)
            return True
        return False
