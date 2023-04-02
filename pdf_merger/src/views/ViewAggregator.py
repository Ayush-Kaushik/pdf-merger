# Author: Ayush Kaushik

from views.ImageToPDFMergeView import ImageToPDFMergeView
from views.PDFCollectionMergeView import PDFCollectionMergeView

class ViewAggregator():
    '''
        Collects all the views to be passed into the main application
    '''
    def __init__(self):
        self.imageToPDFMergeView = ImageToPDFMergeView()
        self.pdfCollectionMergeView = PDFCollectionMergeView()
        
    
        

        

