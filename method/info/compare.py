from gdo.form.GDT_Form import GDT_Form
from gdo.shadowdogs.GDT_ItemArg import GDT_ItemArg
from gdo.shadowdogs.engine.MethodSD import MethodSD
from gdo.shadowdogs.item.Item import Item


class compare(MethodSD):

    @classmethod
    def gdo_trigger(cls) -> str:
        return 'sdcompare'

    @classmethod
    def gdo_trig(cls) -> str:
        return 'sdcmp'

    def gdo_create_form(self, form: GDT_Form) -> None:
        form.add_fields(
            GDT_ItemArg('item').inventory().equipment().not_null(),
            GDT_ItemArg('item2').inventory().equipment().positional(),
        )
        super().gdo_create_form(form)

    def get_item1(self) -> 'Item':
        return self.param_value('item')

    def get_item2(self, item1: 'Item') -> 'Item':
        if item := self.param_value('item2'):
            return item
        item1.get_slot()
        return self.get_player().get_equipment(item1.get_slot())

    async def sd_execute(self):
        item1 = self.get_item1()
        item2 = self.get_item2(item1)  # <-- pass item1

        # if no counterpart, just examine item1
        if not item2:
            return await self.execute_command(f"sdexamine {item1.render_name_wc()}")

        mods1 = item1.all_player_modifiers()
        mods2 = item2.all_player_modifiers()

        # merged ordered keys
        keys = set(mods1.keys()) | set(mods2.keys())

        # build columns (first col is empty header for row labels)
        def fmt(v):
            if isinstance(v, float):
                # trim .0 nicely
                s = f"{v:.2f}".rstrip('0').rstrip('.')
                return s if s else "0"
            return str(v)

        # column widths
        colw = []
        for k in keys:
            v1 = fmt(mods1.get(k, 0))
            v2 = fmt(mods2.get(k, 0))
            colw.append(max(len(k), len(v1), len(v2)))

        # helpers
        def pad(s, w):
            return s.ljust(w)

        # header row
        parts = [""]  # row label cell
        for k, w in zip(keys, colw):
            parts.append(pad(k, w))
        header = " | ".join(parts)

        # row for an item, bold the better value
        def row_for(item_name: str, a: dict, b: dict):
            cells = [item_name]
            for k, w in zip(keys, colw):
                va, vb = a.get(k, 0), b.get(k, 0)
                sa, sb = fmt(va), fmt(vb)
                # bold higher numeric only
                if isinstance(va, (int, float)) and isinstance(vb, (int, float)):
                    if (va > vb):
                        sa = f"**{sa}**"
                    elif (vb > va):
                        pass  # other row will bold
                cells.append(pad(sa, w))
            return " | ".join(cells)

        # names (mark equipped for clarity)
        name1 = item1.render_name_wc()
        name2 = item2.render_name_wc() + " (equipped)"

        row1 = row_for(name1, mods1, mods2)
        row2 = row_for(name2, mods2, mods1)

        # compute left label width
        leftw = max(len(name1), len(name2), 0)
        header = pad("", leftw) + " | " + header[len(" | "):]  # align header’s first empty cell
        row1 = pad(name1, leftw) + " | " + row1[len(name1) + 3:]
        row2 = pad(name2, leftw) + " | " + row2[len(name2) + 3:]

        # separator (optional)
        sep = "-" * len(header)

        table = f"```\n{header}\n{sep}\n{row1}\n{row2}\n```"
        return self._r(table)

    def sd_execute(self):
        item1 = self.get_item1()
        if not (item2 := self.get_item2()):
            return self.execute_command(f"sdexamine {item1.render_name_wc()}")
        mods1 = item1.all_player_modifiers() # dict.items
        mods2 = item2.all_player_modifiers()
        allkeys = ...# merged keys of mods1 and mods2
        # TODO: compare item1 and item2 in a 3 line matrix.
        # headers all keys
        # item1 value
        # item2 value
        # all ascii art table (same col widths), better value in Render.bold
        

