import pathlib
from PyPDF2 import PdfFileMerger


class PDFService:
    '''
    Deals with operations related to PDF merging and creation
    '''
    
    VALID_EXTENSIONS = [".pdf"]

    def __init__(self, merger: PdfFileMerger, pdfFilePathCollection, targetFilePath: pathlib.Path):
        self.merger = merger
        self.filePathList = pdfFilePathCollection
        self.targetFilePath = targetFilePath

    def mergeQueue(self):
        for file in self.filePathList:
            self.merger.append(file)
        self.merger.write(self.targetFilePath)

    def clearQueue(self):
        self.filePathList = []

    def appendToQueue(self, item: pathlib.Path):
        self.filePathList.append(item)

    def setTargetFilePath(self, filePath):
        self.targetFilePath = filePath

    def getTargetFilePath(self):
        return self.targetFilePath
