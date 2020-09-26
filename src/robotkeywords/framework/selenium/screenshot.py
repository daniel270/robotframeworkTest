# ------------------------------------------------------------------------
# Class to capture screenshots either from browser or from display
# ------------------------------------------------------------------------

from robotkeywords.framework.framework import Framework
from robotkeywords.config.operatingsystems import OperatingSystem
from robot.api import logger
from os import path


class ScreenShot:

    @staticmethod
    def capture_screenshot(driver, filename):
        """
        Captures a screenshot to specified file
        If on windows/mac will capture a browser screenshot
        If on linux will capture a display screenshot
        """
        screenshots_dir = Framework.get_screenshots_path()
        filename = filename.replace(' ', '')
        if 'png' not in filename:
            filename = filename + '.png'
        file_path = path.join(screenshots_dir, filename)
        logger.info("Attempting to save screen shot to file: %s" % file_path)
        system = OperatingSystem.get_operating_system()
        driver.get_screenshot_as_file(file_path)
        logger.info("Screen shot saved")
