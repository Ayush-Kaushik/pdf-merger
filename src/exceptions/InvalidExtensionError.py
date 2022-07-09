# Author: Ayush Kaushik

class InvalidExtensionError(Exception):
    """ Exception raised when extension of file to be merged is not valid
    
    Attributes:
        expectedExtensions -- valid file extensions that could be used
    """
    def __init__(self, expectedExtensions):
        self.expectedExtensions = expectedExtensions
        
        expectedExtensionMessage = "Expected file extensions: " + ",".join(expectedExtensions)
        self.message = "[Invalid file extension] " + expectedExtensionMessage
        super().__init__(self.message)