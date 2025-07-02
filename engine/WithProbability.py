from gdo.base.Util import Random


class WithProbability:

    probability: int = 100

    @staticmethod
    def probable_itm(items: list['WithProbability'], probable_none: int = 0) -> 'WithProbability|any|None':
        props = [(item, item.probability) for item in items]
        return WithProbability.probable_item(props, probable_none)

    @staticmethod
    def probable_item(items: list[tuple[any, int]], probable_none: int = 0) -> 'WithProbability|any|None':
        maximum = probable_none
        for item, probability in items:
            maximum += probability
        if maximum <= 0:
            return None
        rand = Random.mrand(0, maximum - 1)
        current = probable_none
        if rand < current:
            return None
        for item, probability in items:
            current += probability
            if current > rand:
                return item
        return None
