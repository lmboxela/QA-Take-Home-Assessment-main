from selenium.webdriver.common.by import By


class Locator:
    # ---- HomePage locators ----
    VERIFY_TEXT = (By.XPATH, "//h1[@class='margin-base-vertical text-center']")
    FORM_VALIDATION = (By.XPATH, "//p[@id='resultDiv']")

    Enter_Integer = (By.ID, "number")

    CALCULATE_BUTTON = (By.XPATH, "//button[@id='getFactorial']")
    TERMS_AND_CONDITIONS = (By.XPATH, "//a[normalize-space()='Terms and Conditions']")
    TERMS_AND_CONDITIONS_COPY = (By.XPATH, "//body")
    PRIVACY = (By.XPATH, "//a[normalize-space()='Privacy']")
    PRIVACY_COPY = (By.XPATH, "//body")

    HEALTH_FORCE = (By.XPATH, "//a[normalize-space()='Healthforce']")