import glob
import importlib
import inspect
import os

from gdo.core.GDT_Enum import GDT_Enum
from gdo.shadowdogs.itembase.data.items import items


class GDT_ItemClass(GDT_Enum):
    def gdo_choices(self) -> dict:
        items.load()

        return     self.load_classes()
        return self._choices

    def gdo_choices(self) -> dict:
        return {}
