# Author: Ayush Kaushik

import pathlib
from typing import List

from PyPDF2 import PdfFileMerger
from .abstract_file_merger_service import AbstractFileMergerService

'''
    Deals with operations related to PDF merging and creation.
'''


class PdfMergerService(AbstractFileMergerService):
    def __init__(
            self,
            merger: PdfFileMerger,
            path_list: List[pathlib.Path],
            target_path: pathlib.Path
    ):
        super().__init__(
            {".pdf": ".pdf"},
            path_list,
            target_path)
        self.merger = merger

    def merge_files(self):
        for file in self.file_list:
            self.merger.append(file)
        self.merger.write(self.target_file_path)
