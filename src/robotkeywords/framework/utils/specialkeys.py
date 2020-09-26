# ------------------------------------------------------------------------------------
# Class to get special key values as defined in selenium.webdriver.common.keys
# ------------------------------------------------------------------------------------

from robot.api import logger


class SpecialKeys:
    special_keys = {
        'BACKSPACE': '\ue003',
        'ENTER': '\ue007',
        'ESCAPE': '\ue00c',
        'END': '\ue010',
        'HOME': '\ue011',
        'RETURN': '\ue006',
        'SPACE': '\ue00d',
        'TAB': '\ue004'
    }

    @staticmethod
    def get_special_key_value(keyname):
        """ Gets the key value of a named key"""
        try:
            key_value = SpecialKeys.special_keys[keyname]
            if key_value is not None:
                return key_value
        except:
            logger.info('No key name found with name: %s' % keyname)
            logger.info('Recognised key names are: %s' % list(SpecialKeys.special_keys))
            raise
