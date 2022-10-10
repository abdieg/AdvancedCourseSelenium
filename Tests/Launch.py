import unittest
import sys
sys.path.append('..')
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from Common.Constant import Constant

class Launch(unittest.TestCase):

    @classmethod
    def setUp(self):
        # self.driver = webdriver.Firefox(service = Service(Constant.firefox_driver_location))
        self.driver = webdriver.Firefox(executable_path = Constant.firefox_driver_location)
        # self.driver = webdriver.edge(executable_path = Constant.edge_driver_location)

        # self.driver = webdriver.Remote(command_executor="http://127.0.0.1:4444",
        #                                desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True})

        # self.driver = webdriver.Remote(command_executor="http://127.0.0.1:4444",
        #                                desired_capabilities={'browserName': 'MicrosoftEdge', 'javascriptEnabled': True})

        self.driver.set_window_size(Constant.screen_width, Constant.screen_height)
        self.driver.get(Constant.app)

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()