# Author: Ayush Kaushik

from PyQt5.QtCore import QUrl
import pathlib
import img2pdf

class ImageService:
    '''
    Deals with operations related to Image to PDF creation and merging
    '''
    
    # Dictionary of valid extensions
    VALID_EXTENSIONS = {
        ".jpg": ".jpg", 
        ".jpeg": ".jpeg"
    }

    def __init__(self, merger: img2pdf, imgFilePathCollection, targetFilePath: pathlib.Path):
        self.merger = merger
        self.filePathList = imgFilePathCollection
        self.targetFilePath = targetFilePath

    def mergeQueue(self):
        try:
            with open(self.targetFilePath, "ab") as f:
                f.write(self.merger.convert(self.filePathList))
        except Exception as exception:
            print("Exception occurs during merging images")
            print(exception)
            f.close()

    def setTargetFilePath(self, filePath):
        self.targetFilePath = filePath
        
    def remove_prefix(self, text, prefix):
        if text.startswith(prefix):
            return text[len(prefix):]
        return text

    def appendToQueue(self, item):
        if type(item) is QUrl:
            modifiedItemPath = self.remove_prefix(item.toString(), "file://")
            self.filePathList.append(modifiedItemPath)
                                             
    def clearQueue(self):
        self.filePathList = []

    def getTargetFilePath(self):
        return self.targetFilePath
    

        
