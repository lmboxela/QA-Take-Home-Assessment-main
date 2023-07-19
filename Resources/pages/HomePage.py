from Resources.pages.BasePage import BasePage
from Resources.Data import TestData
from Resources.Locators import Locator
import requests
import json


class HomePage(BasePage):
    """ Calculator Home Page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    # Validate empty form
    def validate_empty_form(self):
        self.click(Locator.CALCULATE_BUTTON)
        self.assert_element_text(Locator.FORM_VALIDATION, TestData.FORM_VALIDATION_MESSAGE)

    # validate factor of 7

    def validate_factor_of_seven(self):
        self.enter_text(Locator.Enter_Integer, TestData.NUM_SEVEN)
        self.driver.get_screenshot_as_file("enter_num.png")
        self.driver.implicitly_wait(2000000)
        self.click(Locator.CALCULATE_BUTTON)
        self.assert_element_text(Locator.FORM_VALIDATION, TestData.FACTOR_OF_7)
        self.driver.get_screenshot_as_file("seven_factor.png")

        for e in self.driver.get_log('browser'):
            print(e)

    def terms_and_condition(self):
        self.click(Locator.TERMS_AND_CONDITIONS)
        self.assert_element_text(Locator.TERMS_AND_CONDITIONS_COPY, TestData.CONDITION_COPY)

    def privacy(self):

        self.click(Locator.PRIVACY)
        self.assert_element_text(Locator.PRIVACY_COPY, TestData.PRIVACY_TEXT)

    def health_force_link(self):
        self.click(Locator.HEALTH_FORCE)





