# Author: Ayush Kaushik

from pathlib import Path
from typing import List

from PyPDF2 import PdfMerger
from .abstract_file_merger_service import AbstractFileMergerService

'''
    Deals with operations related to PDF merging and creation.
'''


class PdfMergerService(AbstractFileMergerService):
    def __init__(
            self,
            merger: PdfMerger,
            path_list: List[Path],
            target_path: Path
    ):
        super().__init__(
            {".pdf": ".pdf"},
            path_list,
            target_path)
        self.merger = merger

    def merge_files(self) -> bool:
        try:
            for file in self.file_list:
                self.merger.append(str(file))
                # solution: https://docs.python.org/3/library/pathlib.html#general-properties
            self.merger.write(str(self.target_file_path))
            return True
        except Exception as exception:
            print("Exception occurred during merging PDFs")
            print(exception)
            return False
