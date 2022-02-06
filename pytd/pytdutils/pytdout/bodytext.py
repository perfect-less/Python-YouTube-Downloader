from email.mime import audio
from math import floor
from sys import prefix
from typing import List
from pytube import Stream
from pytd.pytdutils import media
from pytd.pytdutils.media import Media
from pytd.pytdutils.pytdout.textblock import TextBlock
from pytd.pytdutils.pytdout.oman import OutputManager, OManState
from pytd.pytdutils.pytdout.progbar import TwoColumnsText, ProgressBar
from pytd.pytdutils.pytdout.templates import OTemplate


class BodyTextBuilder:

    def __init__(self, state: OManState , oman: OutputManager, template: OTemplate) -> None:
        self.state = state
        self.oman = oman
        self.template = template

        self.lines: List[str] = list ()
        self.currentLine: str = ''

    def beginLine (self, media: Media):
        self.media = media
        self.currentLine = ''

        if   (self.state == OManState.parsing):
            self.currentLine = TwoColumnsText ('..parsing '         , self.media.videoTitle, primary= 'left')
        elif (self.state == OManState.processinginput):
            self.currentLine = TwoColumnsText ('..processing '      , self.media.videoTitle, primary= 'left')
        elif (self.state == OManState.selectstream):
            self.currentLine = TwoColumnsText ('..selecting stream ', self.media.videoTitle, primary= 'left')
        elif (self.state == OManState.finaloutput):
            self.currentLine = TwoColumnsText ('..cleaning up '     , self.media.videoTitle, primary= 'left') 

    def finalizeLine (self):

        self.currentLine = TwoColumnsText ('DONE', self.media.videoTitle, primary= 'left')

        # Error Check
        if (self.media.GetErrorMessage () != '' ):
            self.currentLine = TwoColumnsText (self.media.GetErrorMessage (), self.media.videoTitle, primary= 'left')
            # Set current line to <error message> - <video title>

        self.lines.append (self.currentLine)

    def build (self) -> str:
        text = ''

        for te in self.lines:
            text += te + '\n'

        text += self.currentLine + '\n'
        return text

    # Download bar functions
    def updateBar (self, stream: Stream, chunk: bytes, bytes_remaining: int):

        if (self.state != OManState.downloading):
            return
        
        self.currentLine = BuildDownloadBar (self.media, stream, chunk, bytes_remaining)

    def beginPostProcess (self):

        if (self.state != OManState.downloading):
            return
        
        postprocess_msg = self.media.GetPostProcessTypeName()
        self.currentLine = TwoColumnsText (self.media.videoTitle, postprocess_msg + '..', primary= 'left')





def BuildDownloadBar(media: Media, stream: Stream, chunk: bytes, bytes_remaining: int) -> str:

    total_down_num = len (media.downObjects)
    current_proc_num = min (total_down_num, 2) if (stream.type == 'audio') else 1
    process_num_string = '<{}/{}>'.format (current_proc_num, total_down_num)

    if stream.type == 'video':
        prefix = 'Downloading Video {} '.format (process_num_string)
    elif stream.type == 'audio':
        prefix = 'Downloading Audio {} '.format (process_num_string)

    percentage = floor ( 100 * (stream.filesize - bytes_remaining) / stream.filesize )
    suffix = '     {}%'.format (percentage)[-5:]

    bar = ProgressBar (stream.filesize - bytes_remaining, stream.filesize, prefix= prefix, suffix= suffix)

    return TwoColumnsText (media.videoTitle, bar, primary= 'right')


#class DownloadBodyTextBuilder (BodyTextBuilder):









