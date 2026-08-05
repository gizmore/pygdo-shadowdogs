from gdo.shadowdogs.test.ShadowdogsTestCase import ShadowdogsTestCase


class ShadowdogsHackingTest(ShadowdogsTestCase):

    async def test_00_install(self):
        gizmore = await self.fresh_gizmore()
