from gdo.shadowdogs.actions.Action import Action
from gdo.shadowdogs.test.ShadowdogsTestCase import ShadowdogsTestCase
from gdotest.TestUtil import cli_plug


class TestWalkthrough(ShadowdogsTestCase):

    async def test_00_walkthrough(self):
        gizmore = await self.fresh_gizmore()

        out = cli_plug(gizmore, "$sdsearch fr")
        self.assertIn("andwich", out, "search failed")

        out = cli_plug(gizmore, "$sdexplore")
        await self.party_ticker_until(Action.OUTSIDE)

        out = cli_plug(gizmore, "$sdexplore")
        await self.party_ticker_until(Action.OUTSIDE)

        out = cli_plug(gizmore, "$sdexplore")
        await self.party_ticker_until(Action.OUTSIDE)
