from gdo.shadowdogs.WithShadowFunc import WithShadowFunc


class Tile(WithShadowFunc):

    async def visit(self):
        raise NotImplemented()
