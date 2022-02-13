import configparser
import os, sys

CONFIG_FILE_NAME = 'pytdconfig.ini'

def WriteDefaultIniFile():

    config = configparser.ConfigParser()
    config['DEFAULT'] = {'video_codec': 'avc1',
                         'video_adaptive': 'True',
                         'video_down_ext': 'mp4',
                         'video_save_ext': 'mp4',

                         'audio_bitrate': '128kbps',
                         'audio_down_ext': 'mp4',
                         'audio_save_ext': 'mp3',

                         'max_res': '1080',
                         'range_size_denum': '100',
                         'default_file_path': '~/Videos',

                        }

    config['DEFAULT']['default_file_path'] = DetermineDefaultDownloadFolder ()

    # Write config file
    with open( os.path.join(GetThisDir(), CONFIG_FILE_NAME), 'w') as configfile:
        config.write (configfile)

def DetermineDefaultDownloadFolder():
    platform = sys.platform
    download_dir = os.path.join (os.path.expanduser('~'), 'Videos')

    if not os.path.exists (download_dir):
        os.mkdir (download_dir)
    
    return download_dir


def CreateConfigFile():

    if CheckIniFile() == False:
        
        WriteDefaultIniFile ()
        # Create the ini config

def CheckIniFile():

    config_path = GetConfigPath ()

    if os.path.exists(config_path):
        return True
    else:
        return False

def GetConfigPath():
    this_dir = GetThisDir ()
    return os.path.join(this_dir, CONFIG_FILE_NAME)

def GetThisDir():
    return os.path.dirname( os.path.abspath(__file__) )




