from pytd.pytdutils.downloader import DownloadObject
from typing import List

# Media Class
class Media:

    def __init__(self, url: str, mode: str = "both", download_path: str = "~/Videos") -> None:
        self.url = url
        self.mode = mode

        self.downObjects: List[DownloadObject] = list ()
        self.downPath: str = download_path

        self.videoTitle = ''

    def DownloadMedia(self):
        
        for downloadObject in self.downObjects:
            downloadObject.Download()

    def AddDownloadObject(self, newDownloadObject: DownloadObject):
        
        self.downObjects.append(newDownloadObject)
    
    def SetVideoTitle(self, title: str):
        self.videoTitle = title

    def SetFileName(self, fname: str):
        self.filename_path = self.downPath + '/' + fname


    

