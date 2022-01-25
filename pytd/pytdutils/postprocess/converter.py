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

    convert_cmd = 'ffmpeg -i {} -b:a 128K -vn {}'.format(mp4_file, mp3_file)
    subprocess.call (convert_cmd, shell= True)
