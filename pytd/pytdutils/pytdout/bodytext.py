from math import floor
from typing import List
from pytube import Stream

from pytd.pytdutils.media import Media
from pytd.pytdutils.pytdout.omanstate import OManState
from pytd.pytdutils.pytdout.progbar import TwoColumnsText, ProgressBar
from pytd.pytdutils.pytdout.templates import OTemplate


class BodyTextBuilder:

    def __init__(self, state: OManState, template: OTemplate) -> None:
        
        self.state = state
        self.template = template

        self.lines: List[str] = list ()
        self.currentLine: str = ''


    def beginLine (self, media: Media):

        self.media = media
        self.currentLine = _NewLineText (self.state , self.media)
        

    def finalizeLine (self):

        if self.state != OManState.finaloutput:
            self.currentLine = TwoColumnsText ('[✓]', self.media.videoTitle, primary= 'left', sep= '. ')

        # Error Check
        if (self.media.GetErrorMessage () != '' ):
            video_identifier = self.media.videoTitle if self.media.videoTitle else self.media.url
            self.currentLine = TwoColumnsText (video_identifier , self.media.GetErrorMessage (True), primary= 'right', sep= '| ') 
            # Set current line to <error message> - <video title>

        self.lines.append (self.currentLine)
        self.currentLine = ''


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
        
        self.currentLine = _BuildDownloadBar (self.media, stream, chunk, bytes_remaining)

    def beginPostProcess (self):

        if (self.state != OManState.downloading):
            return
        
        postprocess_msg = self.media.GetPostProcessTypeName()
        self.currentLine = TwoColumnsText (self.media.videoTitle, ' [' + postprocess_msg + ']  ', primary= 'right')




def _NewLineText (state: OManState, media: Media):
    currentLine = ''

    if   (state == OManState.parsing):
        currentLine = ' ..'

    elif (state == OManState.processinginput):
        currentLine = TwoColumnsText ('\n>>Processing URL:'  , media.url, primary= 'left', sep= ' ')

    elif (state == OManState.selectstream):
        currentLine = TwoColumnsText ('\n>>Selecting Stream:', media.videoTitle, primary= 'left', sep = ' ')

    elif (state == OManState.cleaningup):
        currentLine = TwoColumnsText ('\n>>Cleaning Up:'     , media.videoTitle, primary= 'left', sep= ' ') 

    elif (state == OManState.finaloutput):
        currentLine = TwoColumnsText (media.videoTitle , media.GetErrorMessage (True), primary= 'right') 
    
    return currentLine


def _BuildDownloadBar(media: Media, stream: Stream, chunk: bytes, bytes_remaining: int) -> str:

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










