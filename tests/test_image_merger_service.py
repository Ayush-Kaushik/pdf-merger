# Author: Ayush Kaushik

import unittest
import img2pdf

from PyPDF2 import PdfReader
from pathlib import Path
from pdf_merger.src.services import ImageMergerService


class TestImagesToPdfService(unittest.TestCase):
    def setUp(self):
        test_path = str(Path(__file__).parent.resolve())
        self.target_file_path = Path(test_path + "/output/test_image_merge_output.pdf")
        self.file_list = [
                Path(test_path + "/data/image/file_example_JPG_1MB.jpg"),
                Path(test_path + "/data/image/file_example_JPG_1MB.jpg")
            ]

        self.service = ImageMergerService(
            img2pdf,
            self.file_list,
            self.target_file_path)

    def test_merge_files(self):
        self.service.merge_files()
        self.assertTrue(self.service.target_file_path.exists())
        self.assertTrue(self.validate_pdf())

    def validate_pdf(self) -> bool:
        try:
            with open(self.target_file_path, 'rb') as file:
                reader = PdfReader(file)
                if len(reader.pages) != len(self.file_list):  # easy to assert since there is one image per file
                    return False

                first_page = reader.pages[0]
                text = first_page.extract_text()
                if text is None:
                    return False
                return True
        except:
            return False

    def test_set_target_path(self):
        new_target_path = Path("./tests/output/image.pdf")
        self.service.set_output_target(new_target_path)
        self.assertEqual(self.service.get_output_target(), new_target_path)

    def test_remove_prefix(self):
        text = "file:///path/to/image.png"
        prefix = "file://"
        self.assertEqual(self.service.remove_prefix(text, prefix), "/path/to/image.png")

    def test_append_files(self):
        new_file_path = Path("/path/to/new_image.jpg")
        self.service.append_file(new_file_path)
        self.assertIn(new_file_path, self.service.file_list)

    def test_clear_list(self):
        self.service.clear_list()
        self.assertEqual(self.service.file_list, [])

    def test_get_output_target(self):
        self.assertEqual(self.service.get_output_target(), self.target_file_path)


if __name__ == '__main__':
    unittest.main()
