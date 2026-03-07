# Author: Ayush Kaushik

"""
     Exception raised when extension of file to be merged is not valid

    Attributes:
        expectedExtensions -- valid file extensions that could be used
"""


class InvalidExtensionError(Exception):
    def __init__(self, expected_extensions):
        self.message = "[Invalid file extension] Expected file extensions: " + ",".join(expected_extensions)
        super().__init__(self.message)
