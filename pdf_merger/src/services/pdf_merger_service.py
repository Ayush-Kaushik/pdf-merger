# Author: Ayush Kaushik

from pathlib import Path
from PyPDF2 import PdfMerger

'''
    Deals with operations related to PDF merging and creation.
'''

class PdfMergerService:

    def __init__(self, merger=PdfMerger):
        self.allowed_file_extensions = ('.pdf')
        self.merger = merger

    def merge_files(self, file_list: list[Path], target_file_path: Path) -> bool:
        """
            Merges the files in the file list into a single file.
        """
        try:
            for file in file_list:
                self.merger.append(str(file))
            
            self.merger.write(str(target_file_path))
            return True
        except Exception as exception:
            print("Exception occurred during merging PDFs")
            print(exception)
            return False
