
from gdo.base.Application import Application
from gdo.base.Util import module_enabled


class InstallShadowdogs:

    @classmethod
    async def install(cls):
        from gdo.shadowdogs.SD_Player import SD_Player
        if not SD_Player.table().get_by_aid('1'):
            SD_Player.blank({
                'p_npc_klass': 'reaper',
                'p_race': 'dragon',
                'p_gender': 'male',
            }).insert()
        await cls.install_favicon()

    @classmethod
    async def install_favicon(cls):
        """Use the Shadowdogs logo only when the site has no favicon yet."""
        if not module_enabled('favicon'):
            return
        from gdo.core.GDO_File import GDO_File
        from gdo.favicon.module_favicon import module_favicon
        favicon = module_favicon.instance()
        if favicon.cfg_favicon_original():
            return
        logo = GDO_File.from_path(
            Application.file_path('gdo/shadowdogs/img/shadowdogs_logo_1024x1024.png')
        ).insert()
        await favicon.save_config_val('favicon', logo.get_id())
