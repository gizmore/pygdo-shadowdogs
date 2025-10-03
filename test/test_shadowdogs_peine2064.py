import unittest

from gdo.shadowdogs.test.ShadowdogsTestCase import ShadowdogsTestCase
from gdotest.TestUtil import cli_plug


class ShadowdogsPeine2064Test(ShadowdogsTestCase):

    async def test_00_home(self):
        gizmore = await self.fresh_gizmore(False)
        out = cli_plug(gizmore, '$sdtalk mom hello')
        self.assertIn('upset', out, 'sdtalk mom hello does not work.')
        out = cli_plug(gizmore, '$sdtalk mom work')
        self.assertIn('home', out, 'sdtalk mom hello does not work.')
        out = cli_plug(gizmore, '$sdtalk mom home')
        self.assertIn('find', out, 'sdtalk mom hello does not work.')
        out = cli_plug(gizmore, '$sdtalk mom home')
        self.assertIn('army', out, 'sdtalk mom hello does not work.')
        out = cli_plug(gizmore, '$sdqus')
        self.assertIn('Etablisment', out, 'sdtalk mom hello does not work.')
        out = cli_plug(gizmore, '$sdgml giz inside Marketpl')
        self.assertIn('Marketplace', out, 'gml mom hello does not work.')
        out = cli_plug(gizmore, '$sdtalk moell hello')
        out = cli_plug(gizmore, '$sdtalk moell home')
        out = cli_plug(gizmore, '$sdtalk moell home')
        out = cli_plug(gizmore, '$sdtalk moell yes')
        self.assertIn('money', out, 'moellring does not work.')
        out = cli_plug(gizmore, '$sdgmi giz 400xNuyen')
        out = cli_plug(gizmore, '$sdtalk moell yes')
        self.assertIn('sleep', out, 'moellring does not work.')
        self.assertIn('accomplished', out, 'moellring does not work.')



if __name__ == '__main__':
    unittest.main()
