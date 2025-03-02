import os
import unittest

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdotest.TestUtil import reinstall_module, WebPlug, GDOTestCase, cli_plug


class ShadowdogsTest(GDOTestCase):

    def setUp(self):
        super().setUp()
        Application.init(os.path.dirname(__file__ + "/../../../../"))
        reinstall_module('shadowdogs')
        loader = ModuleLoader.instance()
        loader.load_modules_db(True)
        loader.init_modules(True, True)
        WebPlug.COOKIES = {}
        Application.init_cli()

    def test_00_start(self):
        cli_plug(None, '$sdstart ')
        pass

if __name__ == '__main__':
    unittest.main()
