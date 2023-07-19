from Resources.Data import TestData
from Resources.Locators import Locator
from Resources.pages.BasePage import BasePage
from Resources.pages.HomePage import HomePage
from tests.base_test import BaseTest


class Test_Calculator(BaseTest):

    def setUp(self):
        super().setUp()

    def test_page_loaded(self):
        """ Page must be loaded successfully"""
        self.homePage = HomePage(self.driver)

        # assert if homepage loaded successfully
        self.assertIn(TestData.APP_TITLE, self.homePage.driver.title)
        self.homePage.assert_element_text(Locator.VERIFY_TEXT, TestData.TEXT_TO_VERIFY)

    def test_empty_field(self):
        """Upon clicking calculate a user must see a validation message"""
        self.homePage = HomePage(self.driver)

        # click the calculate button
        self.homePage.validate_empty_form()

    def test_factor_of_seven(self):
        """ The factor of 7 must be 5040"""
        self.homePage = HomePage(self.driver)
        self.homePage.validate_factor_of_seven()

    def test_terms_and_condition(self):
        self.homePage = HomePage(self.driver)
        self.homePage.terms_and_condition()

    def test_privacy(self):
        self.homePage = HomePage(self.driver)
        self.homePage.privacy()

    def test_health_link(self):
        self.homePage = HomePage(self.driver)

        self.homePage.health_force_link()


