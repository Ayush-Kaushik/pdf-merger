# Author: Ayush Kaushik

import unittest
from pathlib import Path

from PyPDF2 import PdfMerger, PdfReader
from pdf_merger.src.services.pdf_merger_service import PdfMergerService

class TestPdfMergerService(unittest.TestCase):
    def setUp(self):
        test_path = str(Path(__file__).parent.resolve())
        merger = PdfMerger()
        
        self.file_list = [
            Path(test_path + '/data/pdf/FREE_Test_Data_1MB_PDF.pdf'),
            Path(test_path + '/data/pdf/FREE_Test_Data_100KB_PDF.pdf')
        ]
        self.target_file_path = Path(test_path + '/output/test_pdf_merge_output.pdf')
        self.service = PdfMergerService(merger)

    def test_merge_files(self):
        self.service.merge_files(self.file_list, self.target_file_path)
        self.assertTrue(self.validate_pdf())

    def validate_pdf(self) -> bool:
        try:
            with open(self.target_file_path, 'rb') as file:
                reader = PdfReader(file)
                first_page = reader.pages[0]
                text = first_page.extract_text()
                if text is None:
                    return False
                return True
        except:
            return False

if __name__ == '__main__':
    unittest.main()
