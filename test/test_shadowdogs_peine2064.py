import unittest

from gdo.shadowdogs.test.ShadowdogsTestCase import ShadowdogsTestCase
from gdotest.TestUtil import cli_plug


class ShadowdogsPeine2064Test(ShadowdogsTestCase):

    async def test_00_quest_home(self):
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
        out += cli_plug(gizmore, '$sdtalk moell yes')
        self.assertIn('live here', out, 'moellring does not work.')
        self.assertIn('accomplished', out, 'moellring does not work.')
        out = cli_plug(gizmore, '$sdsleep')
        self.assertIn('to bed', out, 'quest no work.')
        out = cli_plug(gizmore, '$sdgmi giz 800xNuyen')
        out += cli_plug(gizmore, '$sdtalk moell rent')
        self.assertIn('accomplished', out, 'quest no work.')

    async def test_10_quest_garage1(self):
        gizmore = await self.fresh_gizmore(False)
        out = cli_plug(gizmore, '$sdgml giz inside Gara')
        self.assertIn('Garage', out, 'gml no work.')
        out = cli_plug(gizmore, '$sdtalk bar work')
        self.assertIn('job', out, 'talk no work.')
        out = cli_plug(gizmore, '$sdtalk bar yes')
        self.assertIn('new quest', out, 'talk no work.')
        out = cli_plug(gizmore, '$sdtalk bar jawoll')
        out = cli_plug(gizmore, '$sdkp')
        self.assertIn('Jawoll', out, 'talk no work.')
        out = cli_plug(gizmore, '$sdgml giz inside Jaw')
        self.assertIn('Jawoll', out, 'gml no work.')
        out = cli_plug(gizmore, '$sdbuy beer 50')
        self.assertIn('LargeBeer', out, 'buy no work.')
        out = cli_plug(gizmore, '$sdgml giz inside Gara')
        self.assertIn('Garage', out, 'gml no work.')
        out = cli_plug(gizmore, '$sdgive bark 40xbee')
        self.assertIn('Barkeep', out, 'gml no work.')
        out = cli_plug(gizmore, '$sdgive bark 11xbee')
        self.assertIn('10', out, 'gmlss no work.')
        self.assertIn('accomplish', out, 'gml no work.')

    async def test_20_quest_bam(self):
        gizmore = await self.fresh_gizmore(False)
        out = cli_plug(gizmore, '$sdgml giz inside Gunz')
        self.assertIn('Gunzelin', out, 'gml no work.')
        out = cli_plug(gizmore, '$sdcourses')
        self.assertIn('Math', out, 'courses no work.')
        out = cli_plug(gizmore, '$sdgmi giz 1000xNuy')
        self.assertIn('1000', out, 'gmi no work.')
        out = cli_plug(gizmore, '$sdlearn mat')
        self.assertIn('Math', out, 'learn no work.')


if __name__ == '__main__':
    unittest.main()
