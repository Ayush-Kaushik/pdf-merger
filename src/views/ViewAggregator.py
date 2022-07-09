# Author: Ayush Kaushik

from src.views.ImageToPDFMergeView import ImageToPDFMergeView
from src.views.PDFCollectionMergeView import PDFCollectionMergeView

class ViewAggregator():
    '''
        Collects all the views to be passed into the main application
    '''
    def __init__(self):
        self.imageToPDFMergeView = ImageToPDFMergeView()
        self.pdfCollectionMergeView = PDFCollectionMergeView()
        
    
        

        

