from gdo.base.Util import Random


class WithProbability:
    probability: int = 100

    @staticmethod
    def probable_item(items: list['WithProbability'], probable_none: int = 0) -> 'WithProbability|any|None':
        maximum = probable_none
        for item in items:
            maximum += item.probability
        if maximum == 0:
            return None
        rand = Random.mrand(0, maximum - 1)
        current = probable_none
        if rand < current:
            return None
        for item in items:
            current += item.probability
            if current > rand:
                return item
        return None
