import os, sys, configparser
from distutils.command.config import config

from pytd.settings import inimaker, conkeys

STRING_KEYS = ['video_codec', 'video_adaptive', 'video_down_ext', 'audio_down_ext', 'video_save_ext',
                   'audio_save_ext',  'audio_bitrate', 'default_file_path']

BOOLEAN_KEYS= ['video_adaptive']

INTEGER_KEYS= ['max_res', 'range_size_denum']



def Init():
    """Initialize configuration feature
    Call this to make sure config file exists and download folder also exists"""

    # Make sure config file exists, and if not create a default one
    inimaker.CreateConfigFile()

    # Make sure download directory exists, make one if not
    _MakeDownloadDirectory()


def _MakeDownloadDirectory():
    filedir = GetDefaultFilePath ()

    if not os.path.exists (filedir):
        os.mkdir (filedir)

def GetDefaultFilePath():
    return GetConfig (conkeys.CONFKEYS.default_file_path)


def GetConfig(key):

    if isinstance(key, conkeys.CONFKEYS):
        key = key.value

    config = configparser.ConfigParser()
    config.read(inimaker.GetConfigPath())    

    if key in STRING_KEYS:
        return str ( config['DEFAULT'][key] )

    elif key in BOOLEAN_KEYS:
        return bool ( config['DEFAULT'][key] )

    elif key in INTEGER_KEYS:
        return int ( config['DEFAULT'][key] )

    elif (key == 'list'):
        return '\n'.join (config['DEFAULT'])


def SetConfig(key: str, value: str):

    if key == 'default':
        inimaker.WriteDefaultIniFile ()
        return '{} were reset to default'.format (os.path.join(inimaker.GetThisDir(), inimaker.CONFIG_FILE_NAME))

    config = configparser.ConfigParser()
    config.read (inimaker.GetConfigPath())

    if key in config['DEFAULT']:
        config['DEFAULT'][key] = value
    else:
        return key + " didn't exist in {} ".format (os.path.join(inimaker.GetThisDir(), inimaker.CONFIG_FILE_NAME))

    with open (os.path.join(inimaker.GetThisDir(), inimaker.CONFIG_FILE_NAME), 'w') as configfile:
        config.write (configfile)

    return key + ' Updated to ' + value

