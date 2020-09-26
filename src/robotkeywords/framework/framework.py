# -----------------------------------------------------------------------------------------------------
# Framework
#
# This file contains framework related functions
#
# ----------------------------------------------------------------------------------------------------

import os
from robot.api import logger
from os import path


class Framework(object):
    __logs_full_path = None
    __screenshots_full_path = None
    __downloads_full_path = None

    @staticmethod
    def setup_output_directories():
        """
        Creates output directories for the framework under sub directory $ROBOTOUT
        The env variable $ROBOTOUT should be set
        Creates sub-directories:
        - screenshots
        - logs
        Sets class level variables with full path to each
        """
        try:
            robot_out = os.environ.get('ROBOTOUT')
            if robot_out is None:
                raise Exception('ROBOTOUT environment variable not set')
            if not path.exists(robot_out):
                raise Exception('ROBOTOUT directory not found: %s' % robot_out)
            logs_full_path = path.join(robot_out, 'logs')
            screenshots_full_path = path.join(robot_out, 'screenshots')
            downloads_full_path = path.join(robot_out, 'downloads')
            if not os.path.isdir(logs_full_path):
                os.mkdir(logs_full_path)
            if not os.path.isdir(screenshots_full_path):
                os.mkdir(screenshots_full_path)
            if not os.path.isdir(downloads_full_path):
                os.mkdir(downloads_full_path)
            Framework.__logs_full_path = logs_full_path
            Framework.__screenshots_full_path = screenshots_full_path
            Framework.__downloads_full_path = downloads_full_path
            logger.info("Created logs directory: %s" % logs_full_path)
            logger.info("Created screenshots directory: %s" % screenshots_full_path)
            logger.info("Created downloads directory: %s" % downloads_full_path)
        except Exception as e:
            logger.error('Unable to create output directories')
            logger.error(str(e))
            raise

    @staticmethod
    def get_logs_path():
        return Framework.__logs_full_path

    @staticmethod
    def get_screenshots_path():
        return Framework.__screenshots_full_path

    @staticmethod
    def get_downloads_path():
        return Framework.__downloads_full_path
