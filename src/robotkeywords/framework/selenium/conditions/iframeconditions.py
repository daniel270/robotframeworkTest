# -----------------------------------------------------------------------
# IFrame Wait Conditions
#
# These are a collection of classes for WebDriverWait specific to IFrames
#
# ------------------------------------------------------------------------

from robotkeywords.config.seleniumsettings import SeleniumSettings


class IFrameSwitchDefaultContent(object):
    """
    An expected condition for switching to default content
    """
    def __call__(self, driver):
        try:
            driver.switch_to.default_content()
            return True
        except Exception:
            return False
        finally:
            driver.implicitly_wait(SeleniumSettings.get_implicit_wait())


class IFrameSwitchToByName(object):
    """
    An expected condition for switching to an IFrame specified by name
    """
    def __init__(self, name):
        self.name = name

    def __call__(self, driver):
        try:
            driver.implicitly_wait(1)
            driver.switch_to.frame(self.name)
            return True
        except Exception:
            return False
        finally:
            driver.implicitly_wait(SeleniumSettings.get_implicit_wait())


class IFrameSwitchToByLocator(object):
    """
    An expected condition for switching to an IFrame specified by a locator
    """
    def __init__(self, locator):
        self.locator_type = locator.locator_type
        self.locator_value = locator.locator_value

    def __call__(self, driver):
        try:
            driver.implicitly_wait(1)
            element = driver.find_element(self.locator_type, self.locator_value)
            driver.switch_to.frame(element)
            return True
        except Exception:
            return False
        finally:
            driver.implicitly_wait(SeleniumSettings.get_implicit_wait())
