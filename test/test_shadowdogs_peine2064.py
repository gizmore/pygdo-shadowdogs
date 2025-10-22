import unittest

from gdo.base.Util import Random
from gdo.shadowdogs.city.y2064.Peine.quests.Hate import Hate
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
        out = cli_plug(gizmore, '$sdtalk Mi hello')
        self.assertIn('Besser als Miehe', out, 'talk#1 no work.')
        out = cli_plug(gizmore, '$sdlearn mat')
        self.assertIn('Math', out, 'learn no work.')
        out = cli_plug(gizmore, '$sdgmk giz 10')
        self.assertIn('You gave', out, 'learn no work.')
        out = cli_plug(gizmore, '$sdlvlup --confirm=1 mat')
        self.assertIn('Math', out, 'lvlup does not work.')
        out = cli_plug(gizmore, '$sdtalk Mi hello')
        self.assertIn('learn', out, 'talk#2 no work.')
        Random.init(31337)
        out = cli_plug(gizmore, '$sdtalk Mi learn')
        self.assertIn('powered by', out, 'talk#2 no work.')
        out = cli_plug(gizmore, '$sdtalk Mi 2t')
        self.assertIn('correct', out, 'talk#3 no work.')
        self.assertIn('accomplish', out, 'talk#3.1 no work.')
        self.assertIn('rewarded with skill', out, 'talk#3.2 no work.')

    async def test_30_quest_hate(self):
        gizmore = await self.fresh_gizmore()
        out = cli_plug(gizmore, '$sdgml giz inside Waff')
        self.assertIn('Kief', out, 'gml no work.')
        out = cli_plug(gizmore, '$sdtalk cash hello')
        self.assertIn('Hello', out, 'talk#1 no work.')
        out = cli_plug(gizmore, '$sdtalk cash work')
        self.assertIn('looking', out, 'talk#2 no work.')
        out = cli_plug(gizmore, '$sdtalk cash yes')
        self.assertIn('quest', out, 'talk#3 no work.')
        out = cli_plug(gizmore, '$sdgmi giz 8xMedki')
        self.assertIn('Medkit', out, 'talk#3 no work.')
        for i in range(Hate.NUM_KILLS):
            cli_plug(gizmore, '$sdgmt giz haider')
            await self.party_ticker_for()
            cli_plug(gizmore, '$sduse Medkit')
            await self.ticker_for()
        out = cli_plug(gizmore, '$sdtalk cash yes')
        self.assertIn('accomplished', out, 'talk#4 no work.')



if __name__ == '__main__':
    unittest.main()
