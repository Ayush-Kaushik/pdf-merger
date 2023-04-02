import unittest
import pathlib
import img2pdf
from PyQt5.QtCore import QUrl
from src.services import ImageService

class TestImageToPDFService(unittest.TestCase):
    def setUp(self):
        self.merger = img2pdf
        self.imgFilePathCollection = ["./pdf_merger/tests/data/image/file_example_JPG_1MB", "./pdf_merger/tests/data/image/file_example_JPG_1MB"]
        self.targetFilePath = pathlib.Path("./pdf_merger/tests/output/test_output.pdf")
        self.imageService = ImageService(self.merger, self.imgFilePathCollection, self.targetFilePath)

    def test_mergeQueue(self):
        self.imageService.mergeQueue()
        self.assertTrue(self.targetFilePath.exists())

    def test_setTargetFilePath(self):
        new_target_path = pathlib.Path("./pdf_merger/tests/output/image.jpg")
        self.imageService.setTargetFilePath(new_target_path)
        self.assertEqual(self.imageService.getTargetFilePath(), new_target_path)

    def test_remove_prefix(self):
        text = "file:///path/to/image.png"
        prefix = "file://"
        self.assertEqual(self.imageService.remove_prefix(text, prefix), "/path/to/image.png")

    def test_appendToQueue(self):
        item = QUrl.fromLocalFile("/path/to/new_image.jpg")
        self.imageService.appendToQueue(item)
        self.assertIn("/path/to/new_image.jpg", self.imageService.filePathList)

    def test_clearQueue(self):
        self.imageService.clearQueue()
        self.assertEqual(self.imageService.filePathList, [])

    def test_getTargetFilePath(self):
        self.assertEqual(self.imageService.getTargetFilePath(), self.targetFilePath)

if __name__ == '__main__':
    unittest.main()