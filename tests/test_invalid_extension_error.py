import unittest
from pdf_merger.src.exceptions.invalid_extension_error import InvalidExtensionError


class TestInvalidExtensionError(unittest.TestCase):

    def test_error_message(self):
        error = InvalidExtensionError(['.jpg', '.png'])
        self.assertEqual(str(error), '[Invalid file extension] Expected file extensions: .jpg,.png')


if __name__ == '__main__':
    unittest.main()
