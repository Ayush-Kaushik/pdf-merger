# Author: Ayush Kaushik

from pdf_merger.src.views.image_to_pdf_merge_view import ImageToPDFMergeView
from pdf_merger.src.views.pdf_collection_merge_view import PDFCollectionMergeView

'''
    Collects all the views to be passed into the main application
'''


class ViewAggregator:
    def __init__(self):
        self.imageToPDFMergeView = ImageToPDFMergeView()
        self.pdfCollectionMergeView = PDFCollectionMergeView()
        
    
        

        

