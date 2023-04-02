import unittest
from unittest.mock import Mock
from PyQt5.QtCore import QUrl
import pathlib
from src.services import ImageService


class TestMergePDFService(unittest.TestCase):

    def setUp(self):
        self.mock_merger = Mock()
        self.imgFilePathCollection = ['test_image1.jpg', 'test_image2.png']
        self.targetFilePath = pathlib.Path(
            './pdf_merger/tests/output/test_output.pdf')
        self.image_service = ImageService(
            self.mock_merger, self.imgFilePathCollection, self.targetFilePath)

    def test_mergeQueue_calls_merger_with_correct_arguments(self):
        self.image_service.mergeQueue()
        self.mock_merger.convert.assert_called_with(self.imgFilePathCollection)

    def test_setTargetFilePath_sets_targetFilePath(self):
        new_target_path = pathlib.Path('./pdf_merger/tests/output')
        self.image_service.setTargetFilePath(new_target_path)
        self.assertEqual(
            self.image_service.getTargetFilePath(), new_target_path)

    def test_remove_prefix_removes_prefix(self):
        text = 'file:///test/path/to/file.jpg'
        prefix = 'file://'
        expected_result = '/test/path/to/file.jpg'
        self.assertEqual(self.image_service.remove_prefix(
            text, prefix), expected_result)

    def test_appendToQueue_adds_item_to_filePathList(self):
        item = QUrl.fromLocalFile(
            './pdf_merger/tests/data/image/file_example_JPG_1MB.jpg')
        self.image_service.appendToQueue(item)
        expected_list = ['test_image1.jpg',
                         'test_image2.png', 'test_image3.jpeg']
        self.assertEqual(self.image_service.filePathList, expected_list)

    def test_clearQueue_clears_filePathList(self):
        self.image_service.clearQueue()
        self.assertEqual(self.image_service.filePathList, [])


if __name__ == '__main__':
    unittest.main()
