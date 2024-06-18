# Author: Ayush Kaushik
from typing import List

from pathlib import Path
import img2pdf
from .abstract_file_merger_service import AbstractFileMergerService

'''
    Operations related to merging Images to PDF.
'''


class ImageMergerService(AbstractFileMergerService):
    def __init__(self, merger: img2pdf, file_list: List[Path], target_path: Path):
        super().__init__({
            ".jpg": ".jpg",
            ".jpeg": ".jpeg",
            ".png": ".png"
        },
            file_list,
            target_path)

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
