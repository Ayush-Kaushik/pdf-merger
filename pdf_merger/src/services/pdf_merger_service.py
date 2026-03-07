# Author: Ayush Kaushik

from PyPDF2 import PdfMerger
from pdf_merger.src.data.merge_job import MergeJob

'''
    Deals with operations related to PDF merging and creation.
'''

class PdfMergerService:

    def __init__(self, merger_cls=PdfMerger):
        self.allowed_file_extensions = ('.pdf',)
        self.merger_cls = merger_cls

    def merge_files(self, merge_job: MergeJob) -> bool:
        """
        Merges the files in the merge_job into a single file.
        Expects merge_job.files: list[Path]
                merge_job.output_file: Path
        """
        try:
            if not merge_job.files:
                print("No files to merge.")
                return False
            if not merge_job.output_file:
                print("Output file not set.")
                return False

            merger = self.merger_cls()
            for file in merge_job.files:
                merger.append(str(file))

            merger.write(str(merge_job.output_file))
            merger.close()
            return True
        except Exception as exception:
            print("Exception occurred during merging PDFs")
            print(exception)
            return False