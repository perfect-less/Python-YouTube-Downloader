from sys import exec_prefix
from typing import List
from unittest import expectedFailure

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
    outputObject.InitProcessingInput ()
    mediaList: List[Media] = InputToMedia (inputObj, outputObject)
    activeMediaList = mediaList.copy ()

    # Select Streams
    outputObject.InitSelectStream ()
    for media in mediaList:

        try:
            selector.Select (media)
        except:
            activeMediaList.remove (media)


    # Download and Process
    outputObject.InitDownloading ()
    for media in activeMediaList:

        try:
            media.DownloadMedia ()
        except:
            activeMediaList.remove (media)
            continue
        
        outputObject.beginPostProcess (media)
        try:
            postprocessor.Post (media)
        except:
            activeMediaList.remove (media)
            continue

    # Done 
    outputObject.InitFinalOutput ()
    print ("Done")
        

    