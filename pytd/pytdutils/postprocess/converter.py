import sys, os
import subprocess
from pytd.pytdutils.media import Media
from pytd.settings.pytdsettings import GetConfig
from pytd.settings.conkeys import CONFKEYS


def ConvertAudio(media: Media):
    if media.mode != 'audio':
        # For now just exit
        # Later Throw Exception or some error handling shall be implemented here
        exit ()

    down_file = media.downObjects[0].file_path
    save_file = media.downObjects[0].file_path [:-len('.'+GetConfig(CONFKEYS.audio_down_ext))] + '.{}'.format(GetConfig(CONFKEYS.audio_save_ext))

    convert_cmd = "ffmpeg -i '{}' -b:a {}K -vn '{}'".format(down_file, GetConfig(CONFKEYS.audio_bitrate) [:-len('kbps')], save_file)
    
    try:
        subprocess.check_call (convert_cmd, shell= True, stdout= subprocess.DEVNULL, stderr= subprocess.STDOUT)
        
    except:
        media.errorMessage = 'Failed converting to {}'.format(GetConfig(CONFKEYS.audio_save_ext))
        media.AddGarbageList (save_file)


