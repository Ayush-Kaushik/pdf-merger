# Author: Ayush Kaushik

from PyQt5.QtCore import QUrl
import pathlib
import img2pdf
from pdf_merger.src.services.merger_service_interface import FileMergerServiceInterface

'''
    Operations related to merging Images to PDF
'''


class ImageService(FileMergerServiceInterface):
    VALID_EXTENSIONS = {
        ".jpg": ".jpg", 
        ".jpeg": ".jpeg",
        ".png": ".png"
    }

    def __init__(self, merger: img2pdf, file_list, target_path: pathlib.Path):
        self.merger = merger
        self.file_list = file_list
        self.target_file_path = target_path

    def merge_files(self):
        try:
            with open(self.target_file_path, "ab") as f:
                f.write(self.merger.convert(self.file_list))
        except Exception as exception:
            print("Exception occurred during merging images")
            print(exception)
            f.close()

    def set_output_target(self, file_path):
        self.target_file_path = file_path
        
    def remove_prefix(self, text, prefix):
        if text.startswith(prefix):
            return text[len(prefix):]
        return text

    def append_file(self, item):
        if type(item) is QUrl:
            modified_path = self.remove_prefix(item.toString(), "file://")
            print(modified_path)
            self.file_list.append(modified_path)
                                             
    def clear_list(self):
        self.file_list = []

    def get_output_target(self):
        return self.target_file_path
    

        
