# ------------------------------------------------------------
# Class for holding an annotation definition for a test case
# ------------------------------------------------------------


class Annotation:

    def __init__(self, class_name, test_name):
        self.testPackage = class_name.split('.')[-1]
        self.testClass = class_name
        self.testMethod = test_name

