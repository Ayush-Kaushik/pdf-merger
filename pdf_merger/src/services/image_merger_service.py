# Author: Ayush Kaushik

from PyQt5.QtCore import QUrl
import pathlib
import img2pdf
from .abstract_file_merger_service import AbstractFileMergerService

'''
    Operations related to merging Images to PDF
'''


class ImageMergerService(AbstractFileMergerService):
    def __init__(self, merger: img2pdf, file_list, target_path: pathlib.Path):
        super().__init__({
            ".jpg": ".jpg",
            ".jpeg": ".jpeg",
            ".png": ".png"
        }, target_path)

        self.merger = merger
        self.file_list = file_list if file_list is not None else []
        self.target_file_path = target_path

    @staticmethod
    def remove_prefix(text: str, prefix: str) -> str:
        """
        Removes the prefix from the given text if present.
        """
        if text.startswith(prefix):
            return text[len(prefix):]
        return text

    def merge_files(self):
        """
        Merges the files in the file list into a single PDF.
        """
        if not self.target_file_path:
            print("Target file path is not set.")
            return
        try:
            with open(self.target_file_path, "ab") as f:
                f.write(self.merger.convert(self.file_list))
            print("Files merged successfully.")
        except Exception as exception:
            print("Exception occurred during merging images")
            print(exception)

    def set_output_target(self, file_path):
        """
        Sets the output target file path.
        """
        self.target_file_path = file_path

    def append_file(self, item):
        """
        Appends a file to the file list.
        """
        if isinstance(item, QUrl):
            modified_path = self.remove_prefix(item.toString(), "file://")
            print(modified_path)
            self.file_list.append(modified_path)
                                             
    def clear_list(self):
        """
        Clears the file list.
        """
        self.file_list = []

    def get_output_target(self):
        """
        Returns the output target file path.
        """
        return self.target_file_path
