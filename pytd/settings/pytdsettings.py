from distutils.command.config import config
from pytd.settings import inimaker, conkeys
import os, sys, configparser

def GetDefaultFilePath():
    return GetValue (conkeys.CONFKEYS.default_file_path)

def Init():
    inimaker.CreateConfigFile()


def GetValue(key: str):

    STRING_KEYS = ['video_codec', 'video_adaptive', 'video_down_ext', 'audio_down_ext', 'video_save_ext',
                   'audio_save_ext',  'audio_bitrate', 'default_file_path']

    BOOLEAN_KEYS= ['video_adaptive']

    INTEGER_KEYS= ['max_res', 'range_size_denum']

    config = configparser.ConfigParser()
    config.read(inimaker.GetConfigPath())


    if key in STRING_KEYS:
        return str ( config['DEFAULT'][key] )
    elif key in BOOLEAN_KEYS:
        return bool ( config['DEFAULT'][key] )
    elif key in INTEGER_KEYS:
        return int ( config['DEFAULT'][key] )
