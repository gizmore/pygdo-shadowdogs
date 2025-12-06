import difflib
from functools import lru_cache
from typing import Any

from gdo.base.Application import Application
from gdo.base.GDT import GDT
from gdo.base.Render import Render
from gdo.base.Trans import Trans
from gdo.core.GDT_String import GDT_String
from gdo.form.GDT_Form import GDT_Form
from gdo.message.GDT_HTML import GDT_HTML
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.lang.shadowhelp import shadowhelp


class help(MethodSD):

    HELP = shadowhelp.HELP

    def sd_requires_player(self) -> bool:
        return False

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdhelp'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdh'

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_field(GDT_String('key').not_null().initial('help').positional())
        super().gdo_create_form(form)

    def _lang(self) -> str:
        return Application.STORAGE.lang

    def _help_root(self) -> dict[str, Any]:
        lang = self.HELP.get(self._lang(), self.HELP['en'])
        root = lang.get('help', {})
        return root if isinstance(root, dict) else {}

    def _find_node(self, key: str) -> tuple[list[str], Any] | None:
        root = self._help_root()
        stack = [([], root)]
        key = key.lower()
        while stack:
            path, node = stack.pop()
            if isinstance(node, dict):
                for k, v in node.items():
                    if k.lower() == key:
                        return (path + [k], v)
                    stack.append((path + [k], v))
        return None

    def _list_subtopics(self, node: dict[str, Any]) -> str:
        intro = node.get("0", "Topics:")
        subs = [k for k in node.keys() if k != "0"]
        if not subs:
            return intro
        # subs.sort(key=str.casefold)
        subs_bold = [f"**{k}**" for k in subs]
        return f"{intro} {', '.join(subs_bold)}."

    def _all_keys(self) -> list[str]:
        keys = []
        stack = [self._help_root()]
        while stack:
            n = stack.pop()
            if isinstance(n, dict):
                for k, v in n.items():
                    if k != "0":
                        keys.append(k.lower())
                    stack.append(v)
        return sorted(set(keys))

    @lru_cache(maxsize=16)
    def _all_keys_cached(self, _lang: str) -> tuple[str, ...]:
        return tuple(self._all_keys())

    def r(self, text: str):
        return GDT_HTML().text(Trans.replace_output(self.replace_output(text)))

    async def sd_execute(self) -> GDT:
        key = self.param_val('key').strip().lower()
        key = "help" if key == "0" else key
        root = self._help_root()

        # case-insensitive top-level check
        root_map = {k.lower(): k for k in root.keys()}
        if key in root_map:
            node = root[root_map[key]]
            if isinstance(node, dict):
                return self.r(self._list_subtopics(node))
            return self.r(str(node))

        hit = self._find_node(key)
        if hit:
            _, node = hit
            if isinstance(node, dict):
                return self.r(self._list_subtopics(node))
            return self.r(str(node))

        if key in ('', 'help', '?'):
            return self.r(self._list_subtopics(root))

        suggestions = difflib.get_close_matches(
            key, self._all_keys_cached(self._lang()), n=5, cutoff=0.5
        )
        if suggestions:
            if len(suggestions) == 1:
                sug = suggestions[0]
                sug_hit = self._find_node(sug)
                if sug_hit:
                    _, node = sug_hit
                    if isinstance(node, dict):
                        return self.r(self._list_subtopics(node))
                    return self.r(str(node))
            return self.err('err_sd_unknown_help_suggest',(', '.join(Render.bold(s, Application.get_mode()) for s in suggestions),))
        return self.err('err_sd_unknown_help', (key, self.get_sd_shortcut()))
