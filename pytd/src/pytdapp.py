from typing import List

from pytd.pytdutils.downloader import DownloadObject, AudioDownloadObject, VideoDownloadObject
from pytd.pytdutils.inputhandler import InputObject, InputToMedia
from pytd.pytdutils.postprocess import postprocessor
from pytd.pytdutils.media import Media
from pytd.pytdutils import downloader
from pytd.pytdutils import selector
from pytd.pytdutils.pytdout.oman import OManState, OutputManager 

def run(inputObj: InputObject, outputObject: OutputManager):

    # Turn Input object to Media objects
    outputObject.report.InitProcessingInput ()
    mediaList: List[Media] = InputToMedia (inputObj, outputObject)
    activeMediaList = mediaList.copy ()

    # Select Streams
    outputObject.report.InitSelectStream ()
    for media in mediaList:
        outputObject.report.beginProcess (OManState.selectstream, media)

        try:
            selector.Select (media, outputObject)
        except:
            activeMediaList.remove (media)
        finally:
            outputObject.report.finishedProcess (OManState.selectstream, media)


    # Download and Process
    outputObject.report.InitDownloading ()
    for media in activeMediaList:
        outputObject.report.beginProcess (OManState.downloading, media)

        try:
            media.DownloadMedia ()
        except:
            activeMediaList.remove (media)
            outputObject.report.finishedProcess (OManState.downloading, media)
            continue
            
        
        outputObject.beginPostProcess ()
        try:
            postprocessor.Post (media)
        except:
            activeMediaList.remove (media)
            outputObject.report.finishedProcess (OManState.downloading, media)

        outputObject.report.finishedProcess (OManState.downloading, media)

    # Done 
    outputObject.report.InitFinalOutput ()
        

    