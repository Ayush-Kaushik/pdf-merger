# Author: Ayush Kaushik
import img2pdf
from pdf_merger.src.data.merge_job import MergeJob

'''
    Operations related to merging Images to PDF.
'''

class ImageMergerService:
    def __init__(self, merger_module=img2pdf):
        self.allowed_file_extensions = (".jpg", ".jpeg", ".png")
        self.merger_module = merger_module

    @staticmethod
    def remove_prefix(text: str, prefix: str) -> str:
        """Removes the prefix from the given text if present."""
        if text.startswith(prefix):
            return text[len(prefix):]
        return text

    def merge_files(self, merge_job: MergeJob) -> bool:
        """
        Merges the files in the merge_job's file list into a single PDF at target_path.
        """
        file_list = merge_job.files
        target_path = merge_job.output_file

        if not file_list:
            print("No files to merge.")
            return False

        if not target_path:
            print("Target file path is not set.")
            return False

        try:
            with open(target_path, "ab") as f:
                # img2pdf requires paths as strings
                f.write(self.merger_module.convert([str(p) for p in file_list]))
            print("Images merged successfully into PDF.")
            return True
        except Exception as e:
            print("Exception occurred during merging images:")
            print(e)
            return False