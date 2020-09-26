# -----------------------------------------------------------------------
# Page/Document Conditions
#
# These are a collection of classes for WebDriverWait specific to DOM pages and documents
#
# ------------------------------------------------------------------------

from robotkeywords.config.seleniumsettings import SeleniumSettings
import time


class DocumentReadyState(object):
    """An expected condition to verify the document ready state"""
    def __call__(self, driver):
        try:
            javascript = "return document.readyState"
            if driver.execute_script(javascript) == "complete":
                return True
            # above actions do not invoke the implicit wait, so sleep instead
            time.sleep(1)
            return False
        except Exception:
            return False


class PageRefresh(object):
    """An expected condition to refresh the page"""
    def __call__(self, driver):
        try:
            driver.refresh()
            return True
        except Exception:
            return False
        finally:
            driver.implicitly_wait(SeleniumSettings.get_implicit_wait())


class PageNavigateBack(object):
    """An expected condition to navigate backwards in the browser history"""
    def __call__(self, driver):
        try:
            driver.back()
            return True
        except Exception:
            return False
        finally:
            driver.implicitly_wait(SeleniumSettings.get_implicit_wait())


class PageNavigateForward(object):
    """An expected condition to navigate forwards in the browser history"""
    def __call__(self, driver):
        try:
            driver.forward()
            return True
        except Exception:
            return False
        finally:
            driver.implicitly_wait(SeleniumSettings.get_implicit_wait())


class PageGetCurrentUrl(object):
    """An expected condition to get the URL of the current page"""
    def __call__(self, driver):
        try:
            javascript = 'return window.location.href'
            url =  driver.execute_script(javascript)
            return url
        except Exception:
            return False
        finally:
            driver.implicitly_wait(SeleniumSettings.get_implicit_wait())

