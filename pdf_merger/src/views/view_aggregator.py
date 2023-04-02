# Author: Ayush Kaushik

from .image_to_pdf_merge_view import ImageToPDFMergeView
from .pdf_collection_merge_view import PDFCollectionMergeView

class ViewAggregator():
    '''
        Collects all the views to be passed into the main application
    '''
    def __init__(self):
        self.imageToPDFMergeView = ImageToPDFMergeView()
        self.pdfCollectionMergeView = PDFCollectionMergeView()
        
    
        

        

