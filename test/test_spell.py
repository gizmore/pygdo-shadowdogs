from gdo.shadowdogs.test.ShadowdogsTestCase import ShadowdogsTestCase
from gdotest.TestUtil import cli_plug, all_private_messages


class ShadowdogsSpellTest(ShadowdogsTestCase):

    async def test_01_calm(self):
        gizmore = await self.fresh_gizmore()
        giz = self.sd_gizmore()
        giz.give_hp(-2)
        hp = giz.gb('p_hp')
        await self.give_spell(giz, 'calm')
        out = cli_plug(gizmore, '$sdcast cal')
        self.assertIn('cal', out, 'cast does not work.')
        await self.ticker(300)
        self.assertGreater(giz.gb('p_hp'), hp, 'calm does not work')

    async def test_02_dart(self):
        gizmore = await self.fresh_gizmore()
        giz = self.sd_gizmore()
        out = cli_plug(gizmore, '$sdgmsp giz dar 2')
        self.assertIn('dart', out, 'gmsp does not work.')
        out = cli_plug(gizmore, '$sdgmt giz lamer')
        await self.ticker(10)
        out = cli_plug(gizmore, '$sdcast dart 1')
        await self.ticker(300)
        out = all_private_messages()
        self.assertIn('kill', out, 'dart does not work.')
