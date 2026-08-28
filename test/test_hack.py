from gdo.shadowdogs.test.ShadowdogsTestCase import ShadowdogsTestCase
from gdotest.TestUtil import cli_plug, all_private_messages


class ShadowdogsHackingTest(ShadowdogsTestCase):

    # Hacking's world setup (PC obstacle/location) is currently stale. Keep
    # this regression disabled until the intended hacking route is restored.
    # async def test_60_hack(self):
    #     gizmore = await self.fresh_gizmore()
    #     target = gizmore.get_name_sid()
    #     out = cli_plug(gizmore, f'$sdgmi {target} RhinoDeck')
    #     self.assertIn('received', out, 'gmi#1 does not work.')
    #     out = cli_plug(gizmore, f'$sdgmi {target} Ping4.exe')
    #     self.assertIn('received', out, 'gmi#2 does not work.')
    #     out = cli_plug(gizmore, '$sdeq Rhino')
    #     self.assertIn('RhinoDeck', out, 'eq#1 does not work.')
    #     await self.ticker(60)
    #     out = all_private_messages()
    #     out += cli_plug(gizmore, '$sdlook')
    #     self.assertIn('PC', out, 'look does not work.')
    #     out = cli_plug(gizmore, '$sdhack')
    #     self.assertIn('PC', out, 'hack does not work.')
    #     out = cli_plug(gizmore, '$sdmov r')
    #     self.assertIn('free', out, 'movr#1 does not work.')
    #     out = cli_plug(gizmore, '$sdmov r')
    #     self.assertIn('vault', out, 'movr#2 does not work.')
