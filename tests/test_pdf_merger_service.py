# Author: Ayush Kaushik

import unittest
from pathlib import Path
from PyPDF2 import PdfMerger

from pdf_merger.src.services.pdf_merger_service import PdfMergerService


class TestPdfMergerService(unittest.TestCase):
    def setUp(self):
        test_path = str(Path(__file__).parent.resolve())
        merger = PdfMerger()
        path_list = [
            Path(test_path + '/data/pdf/FREE_Test_Data_1MB_PDF.pdf'),
            Path(test_path + '/data/pdf/FREE_Test_Data_100KB_PDF')
        ]
        target_path = Path(test_path + '/output/test_output.pdf')
        self.service = PdfMergerService(merger, path_list, target_path)

    def test_merge_files(self):
        self.service.merge_files()
        # TODO check if file exists in the location specified with specific name
        self.assertTrue(self.service.target_file_path.exists())

    def test_clear_list(self):
        self.service.clear_list()
        # TODO perform type check as well for the path list set
        self.assertEqual(len(self.service.file_list), 0)

    def test_append_file(self):
        new_file_path = Path("/path/to/new_image.pdf")
        self.service.append_file(new_file_path)
        self.assertIn(new_file_path, self.service.file_list)

    def test_set_output_target(self):
        new_target_path = Path('new_merged_file.pdf')
        # TODO should set file path have validation?
        self.service.set_output_target(new_target_path)
        self.assertEqual(self.service.get_output_target(), new_target_path)


if __name__ == '__main__':
    unittest.main()
