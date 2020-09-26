# ----------------------------------------------------------------------
# Selenium Keywords
#
# This file contains the selenium robotkeywords for robot framework
# ----------------------------------------------------------------------

"""
This library contains Selenium Robot Framework robotkeywords for Web automation testing.

This library requires:
- ROBOTOUT environment variable to be set. This is where output files and screenshots will be saved to

For locating elements the following element locators are supported:

| =Locator Type= | =Description= | =Example= |
| id | Locates an element using its id attribute | id:username |
| xpath | Locates an element using xpath query on the html dom | xpath://input[@name='uid'] |
| link-text | Locates a hyper link element using its text | link-text:Click Here |
| partial-link-text | Same as link-text but locates the hyper link on partial text match | partial-link-text:username |
| name | Locates an element using the name attribute | name:zipcode |
| tag-name | Locates an element using its html tag name | tag-name:input |
| class-name | Locates an element using its class attribute | class-name:lastname |
| css-selector | Recommended, locates an element using a css query | css-selector:#nameid |

"""

from selenium.webdriver.support.wait import WebDriverWait
from robot.api import logger as robotlogger

from robotkeywords.framework.selenium.conditions.checkboxconditions import *
from robotkeywords.framework.selenium.locator import StringLocator
from robotkeywords.framework.selenium.conditions.elementconditions import *
from robotkeywords.framework.selenium.conditions.iframeconditions import *
from robotkeywords.framework.selenium.conditions.windowconditions import *
from robotkeywords.framework.selenium.driverfactory import DriverFactory
from robotkeywords.framework.selenium.screenshot import ScreenShot

# Module private variables
_driver = None
_default_window = None


# -----------------------------------------------------------
# Driver Keywords
# These are robotkeywords controlling the browser itself
# -----------------------------------------------------------


def driver_open_browser():
    """Opens a web browser"""
    global _driver, _default_window
    _driver = DriverFactory.create_browser()
    _default_window = _driver.current_window_handle
    robotlogger.info('Browser opened with window handle {}'.format(_default_window))


def driver_close_browser():
    """Closes the web browser"""
    global _driver
    if _driver is not None:
        _driver.quit()
        robotlogger.info('Browser closed')
    else:
        robotlogger.info('Browser cannot be closed as it was not opened')


def driver_open_url(url):
    """Opens a specified URL"""
    global _driver
    _driver.get(url)
    robotlogger.info('URL opened {}'.format(url))


def driver_save_screen_shot(filename):
    """Saves a screen shot out of the browser to the screenshots directory with the specified name"""
    ScreenShot.capture_screenshot(_driver, filename)


# ------------------------------------------------------------
# Element Keywords
# These are robotkeywords applicable to many element types
# ------------------------------------------------------------


def element_left_click(locator_string):
    """Left clicks on an element"""
    locator = StringLocator(locator_string)
    robotlogger.info("Left clicking on element: %s" % locator.locator_value)
    wait = WebDriverWait(_driver, SeleniumSettings.get_explicit_wait())
    wait.until(ElementLeftClick(locator))
    robotlogger.info("Element %s was left clicked" % locator_string)


def element_get_text(locator_string):
    """Gets the text of an element - returns text in a string"""
    locator = StringLocator(locator_string)
    wait = WebDriverWait(_driver, SeleniumSettings.get_explicit_wait())
    text = wait.until(ElementGetText(locator))
    robotlogger.info("Element text is: %s" % text)
    return text

# ----------------------------------------------------------------
# Conditions Keywords
# These are robotkeywords waiting for a specific state
# ----------------------------------------------------------------


def element_wait_to_be_displayed(locator_string):
    """Waits for the element to be displayed"""
    robotlogger.info('Waiting for element to be displayed: %s' % locator_string)
    locator = StringLocator(locator_string)
    wait = WebDriverWait(_driver, SeleniumSettings.get_explicit_wait())
    wait.until(ElementWaitForDisplayed(locator))
    robotlogger.info("Element %s was found and is visible" % locator_string)


def element_should_be_displayed(locator_string):
    """Verifies that an element is displayed"""
    locator = StringLocator(locator_string)
    wait = WebDriverWait(_driver, SeleniumSettings.get_explicit_wait())
    wait.until(ElementShouldBeDisplayed(locator))
    robotlogger.info("Element %s was found and is displayed" % locator_string)


def element_should_not_be_displayed(locator_string):
    """Verifies that an element is not displayed"""
    locator = StringLocator(locator_string)
    wait = WebDriverWait(_driver, SeleniumSettings.get_explicit_wait())
    wait.until(ElementShouldNotBeDisplayed(locator))
    robotlogger.info("Element %s was found and is not displayed" % locator_string)


# ------------------------------------------------------------------------
# IFrame Keywords
# These are robotkeywords relating to iframes
# ------------------------------------------------------------------------


def iframe_switch_to_default_content():
    """Switches the browser context back to the document root"""
    wait = WebDriverWait(_driver, SeleniumSettings.get_explicit_wait())
    wait.until(IFrameSwitchDefaultContent())
    robotlogger.info("Switched to default content")


def iframe_switch_to_by_name(name):
    """
    Switches to the iframe specified by its name attribute
    """
    wait = WebDriverWait(_driver, SeleniumSettings.get_explicit_wait())
    wait.until(IFrameSwitchToByName(name))
    robotlogger.info("Switched to iframe with name: %s" % name)


def iframe_switch_to_by_locator(locator_string):
    """Switches to the iframe specified by the locator"""
    locator = StringLocator(locator_string)
    wait = WebDriverWait(_driver, SeleniumSettings.get_explicit_wait())
    wait.until(IFrameSwitchToByLocator(locator))
    robotlogger.info("Switched to iframe with locator: %s" % locator_string)


# -----------------------------------------------------------------------
# Window robotkeywords
# These are robotkeywords for window/tabs
# -----------------------------------------------------------------------

def window_switch_to_main_window():
    """Switches to the base/default window"""
    wait = WebDriverWait(_driver, SeleniumSettings.get_explicit_wait())
    wait.until(WindowSwitchToMainWindow(_default_window))
    robotlogger.info("default window found and switched to it")


def window_maximize_window():
    """Maximizes the current window"""
    wait = WebDriverWait(_driver, SeleniumSettings.get_explicit_wait())
    wait.until(WindowMaximizeWindow())
    robotlogger.info("Maximized the window")


# -----------------------------------------------------------------
# Checkbox Keywords
# Keywords relating to Check box controls
# -----------------------------------------------------------------

def check_box_check(locator_string):
    """Selects the specified check box"""
    locator = StringLocator(locator_string)
    wait = WebDriverWait(_driver, SeleniumSettings.get_explicit_wait())
    wait.until(CheckBoxCheck(locator))
    robotlogger.info("Check box was selected %s" % locator_string)


def check_box_uncheck(locator_string):
    """Un-selects the specified check box"""
    locator = StringLocator(locator_string)
    wait = WebDriverWait(_driver, SeleniumSettings.get_explicit_wait())
    wait.until(CheckBoxUnCheck(locator))
    robotlogger.info("Check box was un-selected %s" % locator_string)
