from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pathlib
import img2pdf

class ImageService:
    '''
    Deals with operations related to Image to PDF creation and merging
    '''
    
    VALID_EXTENSIONS = [".jpg", ".jpeg"]

    def __init__(self, merger: img2pdf, imgFilePathCollection, targetFilePath: pathlib.Path):
        self.merger = merger
        self.filePathList = imgFilePathCollection
        self.targetFilePath = targetFilePath

    def mergeQueue(self):
        for file in self.filePathList:
            print(file)
        try:
            with open(self.targetFilePath, "ab") as f:
                f.write(self.merger.convert(self.filePathList))
        except Exception as exception:
            print(exception)

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

    def appendToQueue(self, item: pathlib.Path):
        self.filePathList.append(item)

    def setTargetFilePath(self, filePath):
        self.targetFilePath = filePath

    def getTargetFilePath(self):
        return self.targetFilePath
    

        
