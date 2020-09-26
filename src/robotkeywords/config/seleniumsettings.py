# -----------------------------------------------------------------------------
# Class to load settings from the seleniumsettings.json file
# ----------------------------------------------------------------------------

import json
import os
from robot.api import logger


class SeleniumSettings:
    """
    Class that loads and exposes the selenium settings from the seleniumsettings.json file
    """
    __json_data = None
    __implicit_wait = None
    __explicit_wait = None
    __script_wait = None
    __page_load_wait = None
    __browser_location = None
    __small_wait = None
    __medium_wait = None
    __long_wait = None

    @staticmethod
    def __get_json_value(key):
        if SeleniumSettings.__json_data is None:
            filename = os.path.abspath(os.path.join(os.path.dirname(__file__), 'seleniumsettings.json'))
            with open(filename, 'r') as json_file:
                raw_data = json_file.read()
                SeleniumSettings.__json_data = json.loads(raw_data)
                logger.info("Selenium settings json file loaded")
        return SeleniumSettings.__json_data[key]

    @staticmethod
    def get_implicit_wait():
        if SeleniumSettings.__implicit_wait is None:
            SeleniumSettings.__implicit_wait = SeleniumSettings.__get_json_value('implicitwait')
        return SeleniumSettings.__implicit_wait

    @staticmethod
    def get_explicit_wait():
        if SeleniumSettings.__explicit_wait is None:
            SeleniumSettings.__explicit_wait = SeleniumSettings.__get_json_value('explicitwait')
        return SeleniumSettings.__explicit_wait

    @staticmethod
    def get_small_wait():
        if SeleniumSettings.__small_wait is None:
            result = SeleniumSettings.__get_json_value('smallwait')
            SeleniumSettings.__small_wait = int(result)
        logger.info("smallwait = %s" % str(SeleniumSettings.__small_wait))
        return SeleniumSettings.__small_wait

    @staticmethod
    def get_medium_wait():
        if SeleniumSettings.__medium_wait is None:
            result = SeleniumSettings.__get_json_value('mediumwait')
            SeleniumSettings.__medium_wait = int(result)
        logger.info("mediumwait = %s" % str(SeleniumSettings.__medium_wait))
        return SeleniumSettings.__medium_wait

    @staticmethod
    def get_long_wait():
        if SeleniumSettings.__long_wait is None:
            result = SeleniumSettings.__get_json_value('longwait')
            SeleniumSettings.__long_wait = int(result)
        logger.info("longwait = %s" % str(SeleniumSettings.__long_wait))
        return SeleniumSettings.__long_wait

    @staticmethod
    def get_script_wait():
        if SeleniumSettings.__script_wait is None:
            result = SeleniumSettings.__get_json_value('scriptwait')
            SeleniumSettings.__script_wait = int(result)
        logger.info("scriptwait = %s" % str(SeleniumSettings.__script_wait))
        return SeleniumSettings.__script_wait

    @staticmethod
    def get_page_load_wait():
        if SeleniumSettings.__page_load_wait is None:
            result = SeleniumSettings.__get_json_value('psgeloadwait')
            SeleniumSettings.__page_load_wait = int(result)
        logger.info("pageloadwait = %s" % str(SeleniumSettings.__page_load_wait))
        return SeleniumSettings.__page_load_wait

    @staticmethod
    def set_implicit_wait(seconds):
        SeleniumSettings.__implicit_wait = seconds

    @staticmethod
    def set_explicit_wait(seconds):
        SeleniumSettings.__explicit_wait = seconds

    @staticmethod
    def set_small_wait(seconds):
        SeleniumSettings.__small_wait = int(seconds)
        logger.info("Small wait set to %s seconds" % str(seconds))

    @staticmethod
    def set_medium_wait(seconds):
        SeleniumSettings.__medium_wait = int(seconds)
        logger.info("Medium wait set to %s seconds" % str(seconds))

    @staticmethod
    def set_long_wait(seconds):
        SeleniumSettings.__long_wait = int(seconds)
        logger.info("Long wait set to %s seconds" % str(seconds))

    @staticmethod
    def set_script_wait(seconds):
        SeleniumSettings.__script_wait = int(seconds)
        logger.info('Script wait set to %s seconds' % str(seconds))

    @staticmethod
    def set_page_load_wait(seconds):
        SeleniumSettings.__page_load_wait = int(seconds)
        logger.info('Page load wait set to %s seconds' % str(seconds))
