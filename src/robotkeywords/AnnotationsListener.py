# ---------------------------------------------------------------------
# Annotations listener
#
# This file implements a robot framework listener for test rail ids
# It gets TestRailIds from the TAGS of the test case
# Only Tags beginning with 'C' are considered TestRail ids
# It then writes the annotations file to $ROBOTOUT/annotations.json
# -------------------------------------------------------------------

from robotkeywords.framework.listeners.annotation import Annotation
from robot.api import logger
import json
import os

ROBOT_LISTENER_API_VERSION = 3
ANNOTATIONS_FILE = 'annotations.json'
SUITE_ANNOTATIONS = []


def end_test(data, result):
    """Called at the end of a test case"""
    logger.info('Start of end_test listener')
    try:
        # get robot data
        test_name = data.name
        full_suite_name = data.parent.longname
        tags = data.tags._tags
        # process to annotations data
        class_name = full_suite_name
        annotation = Annotation(class_name=class_name, test_name=test_name)
        SUITE_ANNOTATIONS.append(annotation)
        logger.info('Test case annotation added to suite annotations')
        logger.info(json.dumps(annotation.__dict__))
    except Exception as e:
        logger.error('Unable to process annotations for test case: %s' % data.name)
        logger.error(e)


def end_suite(data, result):
    """Called at the end of a test suite"""
    logger.info('Start of end_suite listener')
    try:
        json_data = '['
        for item in SUITE_ANNOTATIONS:
            json_data = json_data + json.dumps(item.__dict__) + ','
        json_data = json_data.rstrip(',') + ']'
        robot_out = os.environ.get('ROBOTOUT')
        file_path = os.path.join(robot_out, ANNOTATIONS_FILE)
        with open(file_path, 'w') as json_file:
            json_file.write(json_data)
        logger.info('Annotations file created at: %s' % file_path)
    except Exception as e:
        logger.error('Unable to generate annotations file')
        logger.error(e)
