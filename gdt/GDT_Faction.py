from gdo.core.GDT_Enum import GDT_Enum


class GDT_Faction(GDT_Enum):

    def gdo_choices(self) -> dict:
        return {
            'freeborn': 'Freeborn',
            'council': 'Council',
            'seekers': 'Seekers',
            'aegis': 'Aegis',
        }
