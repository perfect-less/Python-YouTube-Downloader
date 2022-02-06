from inspect import getmodule
from pytd.pytdutils.media import Media
from typing import List
from pytd.pytdutils.pytdout.oman import OutputManager
from pytd.settings import pytdsettings

import os

# Input Object Classs, used to stored Input Data
class InputObject:

    def __init__(self, URLs: List[str], audio_arg, video_arg, use_cwd = False, ) -> None:
        
        self.URLs = URLs
        self.mode = self.GetMode (audio_arg, video_arg)

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
        
        new_media = Media (url, inputObj.mode, inputObj.file_path)
        medias.append (new_media)

    return medias
    
