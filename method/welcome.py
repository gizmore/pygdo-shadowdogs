from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.core.GDT_Container import GDT_Container
from gdo.ui.GDT_Card import GDT_Card
from gdo.ui.GDT_Image import GDT_Image
from gdo.ui.GDT_Link import GDT_Link


class welcome(Method):
    """The public landing page for Shadowdogs."""

    @classmethod
    def gdo_trigger(cls) -> str:
        return ''

    def gdo_render_title(self) -> str:
        return self.t('mt_shadowdogs_welcome', ())

    def gdo_execute(self) -> GDT:
        module = self.gdo_module()
        card = GDT_Card()
        card.title('mt_shadowdogs_welcome')
        card.image(
            GDT_Image('shadowdogs_logo')
            .href(module.www_path('img/shadowdogs_logo_1024x1024.png'))
            .alternate('mt_shadowdogs_welcome')
        )
        content = card.get_content()
        content.add_field(
            GDT_Link('shadowdogs_docs')
            .href(module.www_path('docs/'))
            .text('link_shadowdogs_docs')
            .icon('book')
        )
        return card
