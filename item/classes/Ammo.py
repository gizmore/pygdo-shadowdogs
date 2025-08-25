from gdo.shadowdogs.item.Item import Item


class Ammo(Item):

   def get_default_count(self) -> int:
        return self.dmi('magsize')
