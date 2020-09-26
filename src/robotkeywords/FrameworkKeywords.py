# ---------------------------------------------------------------
# Framework Keywords
#
# This file contains robotkeywords for control of the framework
# ---------------------------------------------------------------

from robot.api import logger
from robotkeywords.config.seleniumsettings import SeleniumSettings
from robotkeywords.framework.framework import Framework


def setup_framework():
    """Main entry point method for the framework"""
    Framework.setup_output_directories()


def close_framework():
    """Closes down the test framework"""


def set_selenium_implicit_wait(seconds):
    """Sets the selenium implicit wait"""
    SeleniumSettings.set_implicit_wait(float(seconds))
    logger.info("Set implicit wait to %s seconds" % str(seconds))


def set_selenium_explicit_wait(seconds):
    """Sets the selenium explicit wait"""
    SeleniumSettings.set_explicit_wait(float(seconds))
    logger.info("Set explicit wait to %s seconds" % str(seconds))


def set_selenium_script_wait(seconds):
    """Sets the selenium javascript wait"""
    SeleniumSettings.set_script_wait(float(seconds))
    logger.info("Set script wait to %s seconds" % str(seconds))


def set_page_load_wait(seconds):
    """Sets the wait time for a page load"""
    SeleniumSettings.set_page_load_wait(float(seconds))
    logger.info("Set page load wait to %s seconds" % str(seconds))
