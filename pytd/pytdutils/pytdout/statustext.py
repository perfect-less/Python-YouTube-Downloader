
from pytd.pytdutils.media import Media
from pytd.pytdutils.pytdout.omanstate import OManState
from pytd.pytdutils.pytdout.progbar import TwoColumnsText, ProgressBar
from pytd.pytdutils.pytdout.templates import OTemplate

from os import get_terminal_size


class StatusTextBuilder:

    def __init__(self, state: OManState, template: OTemplate) -> None:
        self.state = state
        self.template = template
        self.text = ''
    
    def build (self):
        return self.text

    def update (self, media: Media = None):
        self.text = '_'*get_terminal_size().columns + StatusText (self.state, self.template, media)


def StatusText (state: OManState, template: OTemplate, media: Media = None):


    if   (state == OManState.parsing):
        return ParsingText(template, media)
    
    elif (state == OManState.processinginput):
        return ProcessingInputText (template, media)
    
    elif (state == OManState.selectstream):
        return SelectStreamText (template, media)

    elif (state == OManState.downloading):
        return DownloadingText (template, media)

    elif (state == OManState.cleaningup):
        return CleaningUpText (template, media)

    elif (state == OManState.finaloutput):
        return FinalOutputText (template, media)




##
## Actual Text for status
##

def ParsingText(template: OTemplate, media: Media = None):
    return template.status_text

    
def ProcessingInputText(template: OTemplate, media: Media):
    return template.status_text.format (url= media.url)


def SelectStreamText(template: OTemplate, media: Media):
    return template.status_text.format (ytitle= media.url)


def DownloadingText(template: OTemplate, media: Media = None):
    return template.status_text


def CleaningUpText(template: OTemplate, media: Media = None):
    return template.status_text


def FinalOutputText(template: OTemplate, media: Media):
    return template.status_text.format (downdir= media.downPath)
