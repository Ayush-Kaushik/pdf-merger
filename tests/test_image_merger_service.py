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

        self.service = ImageMergerService(img2pdf)

    def test_merge_files(self):
        self.service.merge_files(self.file_list, self.target_file_path)
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

    def test_remove_prefix(self):
        text = "file:///path/to/image.png"
        prefix = "file://"
        self.assertEqual(self.service.remove_prefix(text, prefix), "/path/to/image.png")

if __name__ == '__main__':
    unittest.main()
