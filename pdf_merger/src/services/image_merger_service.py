# Author: Ayush Kaushik

from pathlib import Path
import img2pdf

'''
    Operations related to merging Images to PDF.
'''

class ImageMergerService:
    def __init__(self, merger=img2pdf):
        self.allowed_file_extensions = (".jpg", ".jpeg", ".png")
        self.merger = merger

    @staticmethod
    def remove_prefix(text: str, prefix: str) -> str:
        """
        Removes the prefix from the given text if present.
        """
        if text.startswith(prefix):
            return text[len(prefix):]
        return text

    def merge_files(self, file_list: list[Path], target_path: Path) -> bool:
        """
            Merges the files in the file list into a single file.
        """
        if not target_path:
            print("Target file path is not set.")
            return False
        try:
            with open(target_path, "ab") as f:
                f.write(self.merger.convert(file_list))
            print("Files merged successfully.")
            return True
        except Exception as exception:
            print("Exception occurred during merging images")
            print(exception)
            return False
