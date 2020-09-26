# ----------------------------------------------------------------------------------------
# DriverFactory
#
# Class for creating a browser instance
# The options are:
# - Local browser (on windows)
# - Local browser (on Linux)
# - Local browser (on Mac)
#
# OS detection is automatic
#
# Chrome driver locations:
# - Linux, assume the chrome driver is already installed as part of docker container
# - Mac, assume the chrome driver is already part of the path
# - Windows, chrome driver exe is part of the python package
#
# Chrome downloads directory:
# - This is set to $ROBOTOUT/downloads
# -----------------------------------------------------------------------------------------

from robot.api import logger
from robotkeywords.config.seleniumsettings import SeleniumSettings
from robotkeywords.config.operatingsystems import OperatingSystem
from selenium import webdriver
from os import path
from robotkeywords.framework.framework import Framework


class DriverFactory:

    @staticmethod
    def create_browser():
        """Creates a chrome instance and returns the driver object"""
        logger.debug("Creating chrome instance")
        try:
            system = OperatingSystem.get_operating_system()
            if system == OperatingSystem.Windows:
                driver = DriverFactory.__create_local_windows()
            elif system == OperatingSystem.Linux:
                driver = DriverFactory.__create_local_linux()
            elif system == OperatingSystem.Mac:
                driver = DriverFactory.__create_local_mac()
            else:
                raise Exception("Unsupported browser location and operating system")
            driver.implicitly_wait(SeleniumSettings.get_implicit_wait())
            driver.set_script_timeout(SeleniumSettings.get_script_wait())
            if system != OperatingSystem.Linux:
                driver.fullscreen_window()
                driver.maximize_window()
            return driver
        except Exception as e:
            logger.error("Error creating chrome instance: %s" % e)
            raise

    @staticmethod
    def __create_local_windows():
        """Creates chrome instance on local windows"""
        try:
            options = DriverFactory.__create_options()
            driver_path = DriverFactory.__get_driver_location(OperatingSystem.Windows)
            driver = webdriver.Chrome(options=options, executable_path=driver_path)
            logger.info("Chrome driver instance created for Windows")
            return driver
        except Exception as e:
            logger.error("Unable to create chrome driver on Windows: %s" % e)
            raise

    @staticmethod
    def __create_local_linux():
        """Creates chrome instance on local linux"""
        try:
            options = DriverFactory.__create_options()
            driver_path = DriverFactory.__get_driver_location(OperatingSystem.Linux)
            driver = webdriver.Chrome(options=options, executable_path=driver_path)
            logger.info("Chrome driver instance created for linux")
            return driver
        except Exception as e:
            logger.error("Unable to create chrome driver on Mac: %s" % e)
            raise

    @staticmethod
    def __create_local_mac():
        """Creates chrome instance on local mac"""
        try:
            options = DriverFactory.__create_options()
            driver = webdriver.Chrome(options=options)
            logger.info("Chrome driver instance created for Mac")
            return driver
        except Exception as e:
            logger.error("Unable to create chrome driver on Mac: %s" % e)
            raise

    @staticmethod
    def __create_options():
        """Sets up the chrome options"""
        options = webdriver.ChromeOptions()
        downloads = Framework.get_downloads_path()
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--disable-plugins")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument("--start-maximized")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-background-networking")
        preferences = {
            "download.default_directory": downloads,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        system = OperatingSystem.get_operating_system()
        if system == OperatingSystem.Linux:
            preferences["download.prompt_for_download"] = False
            preferences["download.directory_upgrade"] = True
        options.add_experimental_option("prefs", preferences)
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        return options

    @staticmethod
    def __get_driver_location(system):
        """Gets the location of the driver executable"""
        if system == OperatingSystem.Linux:
            driver_path = '/usr/bin/chromedriver'
            logger.info('Driver path: %s' % driver_path)
            return driver_path
        elif system == OperatingSystem.Windows:
            drivers_dir_path = path.join(path.dirname(path.realpath(__file__)), 'drivers')
            driver_path = path.join(drivers_dir_path, 'chromedriver.exe')
            logger.info('Driver path: %s' % driver_path)
            return driver_path
        else:
            raise Exception("Driver path cannot be created for current OS")

