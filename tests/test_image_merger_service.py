import unittest
import pathlib
import img2pdf
from PyQt5.QtCore import QUrl
from pdf_merger.src.services import ImageMergerService


class TestImagesToPdfService(unittest.TestCase):
    def setUp(self):
        test_path = str(pathlib.Path(__file__).parent.resolve())
        self.target_file_path = pathlib.Path(test_path + "/output/test_output.pdf")

        self.service = ImageMergerService(
            img2pdf,
            [
                pathlib.Path(test_path + "/tests/data/image/file_example_JPG_1MB.jpg"),
                pathlib.Path(test_path + "/tests/data/image/file_example_JPG_1MB.jpg")
            ],
            self.target_file_path)

    def test_merge_files(self):
        self.service.merge_files()
        self.assertTrue(self.service.target_file_path.exists())
        # TODO perform validation by opening the file and check if it can be opened

    def test_set_target_path(self):
        new_target_path = pathlib.Path("./tests/output/image.pdf")
        self.service.set_output_target(new_target_path)
        self.assertEqual(self.service.get_output_target(), new_target_path)

    def test_remove_prefix(self):
        text = "file:///path/to/image.png"
        prefix = "file://"
        self.assertEqual(self.service.remove_prefix(text, prefix), "/path/to/image.png")

    def test_append_files(self):
        new_file_path = QUrl.fromLocalFile("/path/to/new_image.jpg")
        self.service.append_file(new_file_path)
        self.assertIn("/path/to/new_image.jpg", self.service.file_list)

    def test_clear_list(self):
        self.service.clear_list()
        self.assertEqual(self.service.file_list, [])

    def test_get_output_target(self):
        self.assertEqual(self.service.get_output_target(), self.target_file_path)


if __name__ == '__main__':
    unittest.main()
