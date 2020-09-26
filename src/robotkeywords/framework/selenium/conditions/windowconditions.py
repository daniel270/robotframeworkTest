# -----------------------------------------------------------------------
# Window Wait Conditions
#
# These are a collection of classes for WebDriverWait specific to Windows
#
# ------------------------------------------------------------------------

from robotkeywords.config.seleniumsettings import SeleniumSettings
import time


class WindowMaximizeWindow(object):
    """Maximize the window"""
    def __call__(self, driver):
        try:
            driver.maximize_window()
            time.sleep(1)
            return True
        except Exception:
            return False
        finally:
            driver.implicitly_wait(SeleniumSettings.get_implicit_wait())


class WindowSwitchToMainWindow(object):
    """An expected condition to switch to main/base window, window that is opened first at the beginning of test"""
    def __init__(self, default_handle):
        self.default_handle = default_handle

    def __call__(self, driver):
        try:
            driver.implicitly_wait(1)
            handles = driver.window_handles
            for handle in handles:
                if handle == self.default_handle:
                    driver.switch_to.window(handle)
                    return True
            # above actions dont invoke an implicit wait
            time.sleep(1)
            return False
        except Exception:
            return False
        finally:
            driver.implicitly_wait(SeleniumSettings.get_implicit_wait())


