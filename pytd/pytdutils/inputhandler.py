from pytube import YouTube
from typing import List

from pytd.pytdutils.media import Media
from pytd.pytdutils.pytdout.oman import OutputManager
from pytd.pytdutils.pytdout.omanstate import OManState
from pytd.settings import pytdsettings

import os



# Input Object Classs, used to stored Input Data
class InputObject:

    def __init__(
            self, 
            URLs: List[str], 
            audio_arg, 
            video_arg, 
            keep = False, 
            use_cwd = False, 
    ) -> None:
        
        self.URLs = URLs
        self.mode = self.GetMode (audio_arg, video_arg)
        self.keep = keep

        self.file_path = self.GetFilepath(use_cwd)
        

    def GetMode(self, audio_arg, video_arg) -> str:
        
        mode = "both"

        if not (audio_arg == video_arg):

            mode = bool (audio_arg) * "audio" + bool (video_arg) * "video"

        return mode

    def GetFilepath(self, use_cwd: bool) -> str:

        if use_cwd:
            return os.getcwd()
        
        return pytdsettings.GetDefaultFilePath()

# Convert Input Object Into Media Object
def InputToMedia(inputObj: InputObject, outputObject: OutputManager) -> List[Media]:

    medias: List[Media] = list ()

    for url in inputObj.URLs:
        
        new_media = Media (url, inputObj.mode, inputObj.keep, inputObj.file_path)
        outputObject.report.beginProcess (OManState.processinginput, new_media)

        try:
            new_media.SetVideoTitle (YouTube(url).title)
            
        except:
            new_media.errorMessage += "Can't Process URL; "

        medias.append (new_media)
        outputObject.report.finishedProcess (OManState.processinginput, new_media)

    return medias
    
