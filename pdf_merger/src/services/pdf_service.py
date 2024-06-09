# Author: Ayush Kaushik

import pathlib
from PyPDF2 import PdfFileMerger
from pdf_merger.src.services.merger_service_interface import FileMergerServiceInterface

'''
    Deals with operations related to PDF merging and creation
'''


class PDFService(FileMergerServiceInterface):
    VALID_EXTENSIONS = {".pdf" : ".pdf"}

    def __init__(self, merger: PdfFileMerger, path_list, target_path: pathlib.Path):
        self.merger = merger
        self.path_list = path_list
        self.target_file_path = target_path

    def merge_files(self):
        for file in self.path_list:
            self.merger.append(file)
        self.merger.write(self.target_file_path)

    def clear_list(self):
        self.path_list = []

    def append_file(self, file_path: pathlib.Path):
        self.path_list.append(str(file_path.toLocalFile()))

    def set_output_target(self, file_path):
        self.target_file_path = file_path

    def get_output_target(self):
        return self.target_file_path
