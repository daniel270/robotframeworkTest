# -------------------------------------------------------
# Custom locator string class
#
# This class parses a string into a valid locator
# The string format is: <locator-type>:<locator-value>
# With possible locator types as:
# - id
# - xpath
# - link-text
# - partial-link-text
# - name
# - tag-name
# - class-name
# - css-selector
#
# -------------------------------------------------------


class LocatorParseError(Exception):
    """ Exception for parsing a locator string """
    pass


class StringLocator(object):
    __valid_locator_types = ["id", "xpath", "link-text", "partial-link-text", "name", "tag-name", "class-name",
                             "css-selector"]

    def __init__(self, locator_string):
        self.locator_type, self.locator_value = self.__parse_string(locator_string)

    # Parses the string into two parts, locator-type, locator-value
    # Throws a LocatorParseError if cannot parse the string
    def __parse_string(self, locator_string):
        try:
            locator_parts = locator_string.split(':', 1)
            parts_count = len(locator_parts)
            if parts_count != 2:
                raise Exception("Invalid locator, type or value not specified")
            locator_type = locator_parts[0]
            locator_value = locator_parts[1]
            if locator_type not in self.__valid_locator_types:
                raise Exception("Invalid locator type: %s" % locator_type)
            if len(locator_value) <= 1:
                raise Exception("Invalid locator value: %s" % locator_value)
            selenium_locator_type = locator_type.replace('-', ' ')
            return selenium_locator_type, locator_value
        except Exception as e:
            raise LocatorParseError(e)
