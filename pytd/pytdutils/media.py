from distutils.log import error
from statistics import mode
from pytd.pytdutils.downloader import DownloadObject
from typing import List
import os

# Media Class
class Media:

    def __init__(

            self, 
            url: str, 
            mode: str = "both", 
            keep: bool = False, 
            download_path: str = "~/Videos"

    ) -> None:

        self.url = url
        self.mode = mode
        self.keep = keep

        self.downObjects: List[DownloadObject] = list ()
        self.downPath: str = download_path

        self.videoTitle = ''
        self.errorMessage = ''

        self.garbageList: List[str] = list ()

    def DownloadMedia(self):
        
        for downloadObject in self.downObjects:
            downloadObject.Download()

    def AddDownloadObject(self, newDownloadObject: DownloadObject):
        
        self.downObjects.append(newDownloadObject)
        self.AddGarbageList (newDownloadObject.GetFilePath ())
    
    def SetVideoTitle(self, title: str):
        self.videoTitle = title

    def SetFileName(self, fname: str):
        self.filename_path = os.path.join (self.downPath, fname)

    def GetErrorMessage (self, msg: bool = False) -> str:
        if (msg == True) and (self.errorMessage == ''):
            return '   Succesfully Downloded   '

        return self.errorMessage

    def GetPostProcessTypeName (self) -> str:
        
        if (self.mode == 'both'):
            return 'Merging'
        else:
            return 'Converting'

    def AddGarbageList (self, new_garbage_file: str):

        if self.keep == True: 
            return
        # Add Garbage List if keep is false
        self.garbageList.append (new_garbage_file)

    def RemoveFromGarbageList (self, path_to_file: str):
        self.garbageList.remove (path_to_file)

    def GetGarbageList (self):
        return self.garbageList

    def DeleteGarbage(self):
        pass

        # Delete All File self.garbageList


    

