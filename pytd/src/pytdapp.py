from typing import List

from pytd.pytdutils.downloader import DownloadObject, AudioDownloadObject, VideoDownloadObject
from pytd.pytdutils.inputhandler import InputObject, InputToMedia
from pytd.pytdutils.postprocess import postprocessor
from pytd.pytdutils.media import Media
from pytd.pytdutils import downloader
from pytd.pytdutils import selector
from pytd.pytdutils.pytdout.oman import OutputManager 

def run(inputObj: InputObject, outputObject: OutputManager):

    print ("Begin")

    # Turn Input object to Media objects
    mediaList: List[Media] = InputToMedia (inputObj)

    # Select Streams
    for media in mediaList:
        selector.Select (media)

    # Download and Process
    for media in mediaList:
        media.DownloadMedia ()
        postprocessor.Post (media)

    # Done 
    print ("Done")
        

    