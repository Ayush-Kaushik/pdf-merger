# Author: Ayush Kaushik

from pdf_merger.src.ui.file_collection_merge_view import FileCollectionMergeView
from pdf_merger.src.data.merge_job import MergeJob


class ViewAggregator:

    def __init__(self, labels, pdf_merger_service, image_merger_service):

        self.labels = labels

        self.pdf_merger_service = pdf_merger_service
        self.image_merger_service = image_merger_service

        self._build_pdf_merge_view()
        self._build_image_merge_view()

    # ---------------------------------------------------------
    # PDF MERGE
    # ---------------------------------------------------------

    def _build_pdf_merge_view(self):

        self.pdf_merge_job = MergeJob()

        self.pdf_collection_merge_view = FileCollectionMergeView(
            labels=self.labels,
            accepted_file_types="*.pdf",
            accept_extensions=[".pdf"],
            mode="pdf"
        )

        view = self.pdf_collection_merge_view

        view.filesSelected.connect(self.pdf_merge_job.add_files)
        view.outputSelected.connect(self.pdf_merge_job.set_output_target)

        view.mergeRequested.connect(self._execute_pdf_merge)
        view.resetRequested.connect(self._reset_pdf_job)

    def _execute_pdf_merge(self):

        success = self.pdf_merger_service.merge_files(self.pdf_merge_job)

        if success:
            self.pdf_collection_merge_view.show_success(
                "PDF files merged successfully."
            )
            self._reset_pdf_job()
        else:
            self.pdf_collection_merge_view.show_failure(
                "Failed to merge PDF files."
            )

    def _reset_pdf_job(self):

        self.pdf_merge_job.clear_files()
        self.pdf_collection_merge_view.reset_view()

    # ---------------------------------------------------------
    # IMAGE MERGE
    # ---------------------------------------------------------

    def _build_image_merge_view(self):

        self.image_merge_job = MergeJob()

        self.image_to_pdf_merge_view = FileCollectionMergeView(
            labels=self.labels,
            accepted_file_types="*.png *.jpg *.jpeg",
            accept_extensions=[".png", ".jpg", ".jpeg"],
            mode="image"
        )

        view = self.image_to_pdf_merge_view

        view.filesSelected.connect(self.image_merge_job.add_files)
        view.outputSelected.connect(self.image_merge_job.set_output_target)

        view.mergeRequested.connect(self._execute_image_merge)
        view.resetRequested.connect(self._reset_image_job)

    def _execute_image_merge(self):

        success = self.image_merger_service.merge_files(self.image_merge_job)

        if success:
            self.image_to_pdf_merge_view.show_success(
                "Images merged into PDF successfully."
            )
            self._reset_image_job()
        else:
            self.image_to_pdf_merge_view.show_failure(
                "Failed to merge images."
            )

    def _reset_image_job(self):

        self.image_merge_job.clear_files()
        self.image_to_pdf_merge_view.reset_view()