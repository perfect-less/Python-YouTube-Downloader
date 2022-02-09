import os
from typing import List
from pytd.pytdutils.media import Media
from pytd.pytdutils.pytdout.oman import OutputManager
from pytd.pytdutils.pytdout.omanstate import OManState

def CleanGarbage (outputObject: OutputManager, mediaList: List[Media]):

    for media in mediaList:

        outputObject.report.beginProcess (OManState.cleaningup, media)
        garbageList = media.GetGarbageList ()
        
        for garbage_path in garbageList:

            DeleteFile (garbage_path)

        outputObject.report.finishedProcess (OManState.cleaningup, media)


def DeleteFile (path: str):

    if os.path.exists (path):
        os.remove (path)
