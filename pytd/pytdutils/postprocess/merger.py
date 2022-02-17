from pytd.pytdutils.downloader import AudioDownloadObject, VideoDownloadObject
from pytd.pytdutils.media import Media

import subprocess


def Merge(media: Media) -> None:

    for downObject in media.downObjects:
        if isinstance (downObject, AudioDownloadObject):
            audioObject = downObject
        if isinstance (downObject, VideoDownloadObject):
            videoObject = downObject

    mergeAudioVideo (audioObject, videoObject, media)

        
def mergeAudioVideo (audioObject: AudioDownloadObject, videoObject: VideoDownloadObject, media: Media):
    audio_path = audioObject.file_path
    video_path = videoObject.file_path
    
    combine_command = "ffmpeg -y -i '{}'  -r 30 -i '{}'  -filter:a aresample=async=1 -c:a flac -strict -2 -c:v copy '{}'".format(audio_path, video_path, media.filename_path)

    try:
        subprocess.check_call (combine_command, shell= True, stdout= subprocess.DEVNULL, stderr= subprocess.STDOUT)
    except Exception as e:
        media.errorMessage += 'Failed merging audio and video; {}'.format (''.join(e.args))
        media.AddGarbageList (media.filename_path)