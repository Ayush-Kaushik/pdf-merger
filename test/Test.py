# Author: Ayush Kaushik

import unittest
from Program import PDFService

class TestPDFMergerApp(unittest.TestCase):
    
    def test_clearPDFQueue(self):
        PDFService.clearPDFQueue(self)
        self.assertEqual(PDFService.getFilePathList(self), [])
        
    # fix this test case    
    def test_appendValidItemToPDFQueue(self):
        filePath = "somefile.pdf"
        PDFService.appendToPDFQueue(filePath)
        pathList = PDFService.getFilePathList(self)
        self.assertCountEqual(len(pathList), 1)