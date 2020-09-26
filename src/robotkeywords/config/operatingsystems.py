# ---------------------------------------------------------
# OperatingSystem
#
# Defines an enum and method to get the current operating system
#
# -----------------------------------------------------------

from enum import Enum
import platform


class OperatingSystem(Enum):
    Windows = 1,
    Linux = 2,
    Mac = 3

    @staticmethod
    def get_operating_system():
        result = platform.system()
        if result == 'Windows':
            return OperatingSystem.Windows
        elif result == 'Linux':
            return OperatingSystem.Linux
        elif result == 'Darwin':
            return OperatingSystem.Mac
        else:
            raise Exception("Unknown operating system: %s" % result)
