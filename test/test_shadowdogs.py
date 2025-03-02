import os
import unittest

from gdo.base.Application import Application
from gdo.base.ModuleLoader import ModuleLoader
from gdo.core.GDO_User import GDO_User
from gdo.core.connector.Web import Web
from gdo.register.module_register import module_register
from gdotest.TestUtil import reinstall_module, web_plug, WebPlug, GDOTestCase


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
        pass

if __name__ == '__main__':
    unittest.main()
