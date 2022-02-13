import sys, os
import subprocess
from pytd.pytdutils.media import Media


def ConvertAudio(media: Media):
    if media.mode != 'audio':
        # For now just exit
        # Later Throw Exception or some error handling shall be implemented here
        exit ()

    mp4_file = media.downObjects[0].file_path
    mp3_file = media.downObjects[0].file_path.removesuffix('.mp4') + '.mp3'

    convert_cmd = "ffmpeg -i '{}' -b:a 128K -vn '{}'".format(mp4_file, mp3_file)
    
    try:
        subprocess.check_call (convert_cmd, shell= True, stdout= subprocess.DEVNULL, stderr= subprocess.STDOUT)
        
    except:
        media.errorMessage = 'Failed converting to mp3'
        media.AddGarbageList (mp3_file)


