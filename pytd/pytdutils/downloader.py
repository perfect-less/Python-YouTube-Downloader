from asyncio import streams
from pytube.streams import Stream

import pytube.request

class DownloadObject:

    def __init__(self, stream: Stream, download_path: str) -> None:
        self.stream = stream
        self.download_path = download_path + '/'
        self.file_name = self.DetermineFilename ()
        self.file_path = self.DetermineFilepath (download_path)

    def Download(self):

        pytube.request.default_range_size = int (min ( self.stream.filesize / 50, 9437184))
        self.stream.download(output_path= self.download_path, filename= self.file_name)

    def DetermineFilename (self):
        return self.stream.default_filename

    def DetermineFilepath(self, download_path: str):
        new_filename = self.DetermineFilename()
        return download_path + '/' + new_filename


class AudioDownloadObject (DownloadObject):

    def DetermineFilename(self):
        return self.stream.default_filename.removesuffix('.mp4') + '_audio.mp4'


class VideoDownloadObject (DownloadObject):

    def DetermineFilename(self):
        return self.stream.default_filename.removesuffix('.mp4') + '_video.mp4'
        
