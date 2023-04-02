import unittest
from src.exceptions.invalid_extension_error import InvalidExtensionError

class TestInvalidExtensionError(unittest.TestCase):

    def test_expected_extensions(self):
        error = InvalidExtensionError(['.jpg', '.png'])
        self.assertEqual(error.expectedExtensions, ['.jpg', '.png'])

    def test_error_message(self):
        error = InvalidExtensionError(['.jpg', '.png'])
        self.assertEqual(str(error), '[Invalid file extension] Expected file extensions: .jpg,.png')

if __name__ == '__main__':
    unittest.main()