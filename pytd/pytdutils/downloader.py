from pytube.streams import Stream
from pytd.settings.pytdsettings import GetConfig
from pytd.settings.conkeys import CONFKEYS

import pytube.request
import os

class DownloadObject:

    def __init__(self, stream: Stream, download_path: str) -> None:
        self.stream = stream
        self.download_path = download_path
        self.file_name = self.DetermineFilename ()
        self.file_path = self.DetermineFilepath (download_path)

    def Download(self):

        pytube.request.default_range_size = int (min ( self.stream.filesize / GetConfig(CONFKEYS.range_size_denum), 9437184))
        self.stream.download(output_path= self.download_path, filename= self.file_name)

    def DetermineFilename (self):
        return self.stream.default_filename

    def DetermineFilepath(self, download_path: str):
        new_filename = self.DetermineFilename()
        return os.path.join (download_path, new_filename)

    def GetFilePath (self):
        return self.file_path


class AudioDownloadObject (DownloadObject):

    def DetermineFilename(self):
        return self.stream.default_filename [:-len('.'+GetConfig(CONFKEYS.audio_down_ext))] + '_audio.{}'.format(GetConfig(CONFKEYS.audio_down_ext))
        # Remove suffix, not using .removesuffix to support python 3.8

class VideoDownloadObject (DownloadObject):

    def DetermineFilename(self):
        return self.stream.default_filename [:-len('.'+GetConfig(CONFKEYS.video_down_ext))] + '_video.{}'.format(GetConfig(CONFKEYS.video_down_ext))
        # Remove suffix, like line 36
        
