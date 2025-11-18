from gdo.base.Trans import t

from typing import TYPE_CHECKING

from gdo.base.Util import html

if TYPE_CHECKING:
    from gdo.shadowdogs.SD_Item import SD_Item


class ShadowdogsException(Exception):

    def __init__(self, key: str, args: tuple[str|int|float|None, ...] = None):
        super().__init__(t(key, args))

class SDTooMuchMatchesException(ShadowdogsException):

    def __init__(self, matches: list['SD_Item']):
        match_str = ", ".join([match.render_name() for match in matches])
        super().__init__('sd_too_much_matches', (match_str,))

class SDUnknownItemException(ShadowdogsException):
    def __init__(self, arg: str):
        super().__init__('sd_unknown_item', (html(arg), ))