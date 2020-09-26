# ---------------------------------------------------------------------------------
# Checkbox Wait Conditions
#
# These are a collection of classes for WebDriverWait specific to Check boxes
#
# --------------------------------------------------------------------------------

from robotkeywords.config.seleniumsettings import SeleniumSettings


class CheckBoxCheck(object):
    """Condition to check/select a check box"""

    def __init__(self, locator):
        self.locator_type = locator.locator_type
        self.locator_value = locator.locator_value

    def __call__(self, driver):
        try:
            driver.implicitly_wait(1)
            element = driver.find_element(self.locator_type, self.locator_value)
            if not element.is_selected():
                element.click()
            return True
        except Exception:
            return False
        finally:
            driver.implicitly_wait(SeleniumSettings.get_implicit_wait())


class CheckBoxUnCheck(object):
    """Condition to uncheck a check box"""
    def __init__(self, locator):
        self.locator_type = locator.locator_type
        self.locator_value = locator.locator_value

    def __call__(self, driver):
        try:
            driver.implicitly_wait(1)
            element = driver.find_element(self.locator_type, self.locator_value)
            if element.is_selected():
                element.click()
            return not element.is_selected()
        except Exception:
            return False
        finally:
            driver.implicitly_wait(SeleniumSettings.get_implicit_wait())
