# -----------------------------------------------------------------------
# Element Wait Conditions
#
# These are a collection of classes for WebDriverWait specific to Elements
#
# ------------------------------------------------------------------------

import os

from selenium.common.exceptions import *
from robotkeywords.config.seleniumsettings import SeleniumSettings


class ElementEnterText(object):
    """
    An expected condition for entering text into an element
    """

    def __init__(self, locator, text):
        self.locator_type = locator.locator_type
        self.locator_value = locator.locator_value
        self.text = text

    def __call__(self, driver):
        try:
            driver.implicitly_wait(1)
            element = driver.find_element(self.locator_type, self.locator_value)
            element.clear()
            element.send_keys(self.text)
            actual_text = element.text
            actual_value = element.get_attribute('value')
            if actual_text is None:
                actual_text = ''
            if actual_value is None:
                actual_value = ''
            return actual_text.strip() == self.text or actual_value.strip() == self.text
        except Exception:
            return False
        finally:
            driver.implicitly_wait(SeleniumSettings.get_implicit_wait())


class ElementLeftClick(object):
    """
    An expected condition for left clicking on an element
    """

    def __init__(self, locator):
        self.locator_type = locator.locator_type
        self.locator_value = locator.locator_value

    def __call__(self, driver):
        try:
            driver.implicitly_wait(1)
            element = driver.find_element(self.locator_type, self.locator_value)
            element.click()
            return True
        except Exception:
            return False
        finally:
            driver.implicitly_wait(SeleniumSettings.get_implicit_wait())


class ElementWaitForDisplayed(object):
    """
    An expected condition for waiting for a displayed element
    """

    def __init__(self, locator):
        self.locator_type = locator.locator_type
        self.locator_value = locator.locator_value

    def __call__(self, driver):
        try:
            driver.implicitly_wait(1)
            element = driver.find_element(self.locator_type, self.locator_value)
            return element.is_displayed()
        except Exception:
            return False
        finally:
            driver.implicitly_wait(SeleniumSettings.get_implicit_wait())


class ElementShouldBeDisplayed(object):
    """
    An expected condition for verifying that an element is displayed
    """

    def __init__(self, locator):
        self.locator_type = locator.locator_type
        self.locator_value = locator.locator_value

    def __call__(self, driver):
        try:
            element = driver.find_element(self.locator_type, self.locator_value)
            return element.is_displayed()
        except Exception:
            return False
        finally:
            driver.implicitly_wait(SeleniumSettings.get_implicit_wait())


class ElementShouldNotBeDisplayed(object):
    """
    An expected condition for verifying that an element is not displayed
    """

    def __init__(self, locator):
        self.locator_type = locator.locator_type
        self.locator_value = locator.locator_value

    def __call__(self, driver):
        try:
            element = driver.find_element(self.locator_type, self.locator_value)
            return not element.is_displayed()
        except NoSuchElementException:
            return True
        except Exception:
            return False
        finally:
            driver.implicitly_wait(SeleniumSettings.get_implicit_wait())


class ElementGetText(object):
    """
    An expected condition to get the text of an element
    Returns a String containing the elements text
    """

    def __init__(self, locator):
        self.locator_type = locator.locator_type
        self.locator_value = locator.locator_value

    def __call__(self, driver):
        try:
            driver.implicitly_wait(1)
            element = driver.find_element(self.locator_type, self.locator_value)
            element_text = element.text
            return element_text.strip()
        except Exception:
            return False
        finally:
            driver.implicitly_wait(SeleniumSettings.get_implicit_wait())

