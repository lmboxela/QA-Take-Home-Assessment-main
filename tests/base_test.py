import unittest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver


class BaseTest(unittest.TestCase):

    def setUp(self):
        dc = DesiredCapabilities.CHROME
        dc['goog:loggingPrefs'] = {'browser': 'ALL'}
        self.driver = webdriver.Chrome()

        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
